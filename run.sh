#!/usr/bin/env bash
# One-command setup and run for TestProject on macOS (or Linux).
#
#   bash run.sh          -> run with SQLite (recommended, nothing else to install)
#   bash run.sh mysql    -> run with MySQL (installs/starts it via Homebrew)
#
# Safe to run again any time; it only does what's still needed.

set -euo pipefail
cd "$(dirname "$0")"

MODE="${1:-sqlite}"

say() { printf '\n\033[1;34m==> %s\033[0m\n' "$1"; }
fail() { printf '\n\033[1;31mERROR: %s\033[0m\n' "$1"; exit 1; }

# 1. Python ------------------------------------------------------------------
command -v python3 >/dev/null 2>&1 || fail "python3 not found. Install it from https://www.python.org/downloads/ or with: brew install python"
python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' \
  || fail "Python 3.10 or newer is required (you have $(python3 --version))."

# 2. Virtual environment + packages -----------------------------------------
# Rebuild the environment if it's missing or broken (e.g. a damaged pip).
if [ ! -x .venv/bin/python ] || ! .venv/bin/python -m pip --version >/dev/null 2>&1; then
  if [ -d .venv ]; then
    say "Existing .venv is broken -- rebuilding it"
    rm -rf .venv
  fi
  say "Creating virtual environment (.venv)"
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

say "Installing Python packages"
python -m pip install --quiet -r requirements.txt

# 3. Database ----------------------------------------------------------------
if [ "$MODE" = "mysql" ]; then
  export DB_ENGINE=mysql
  python -m pip install --quiet "PyMySQL[rsa]>=1.1"

  command -v brew >/dev/null 2>&1 || fail "Homebrew is required for MySQL mode. Install it from https://brew.sh, or just run: bash run.sh"
  if ! brew list mysql >/dev/null 2>&1; then
    say "Installing MySQL with Homebrew (this can take a few minutes)"
    brew install mysql
  fi
  say "Starting MySQL"
  brew services start mysql >/dev/null 2>&1 || true

  MYSQL_ARGS=(-u "${DB_USER:-root}" -h 127.0.0.1)
  [ -n "${DB_PASSWORD:-}" ] && MYSQL_ARGS+=("-p${DB_PASSWORD}")

  for _ in $(seq 1 30); do
    mysqladmin "${MYSQL_ARGS[@]}" ping >/dev/null 2>&1 && break
    sleep 1
  done
  mysqladmin "${MYSQL_ARGS[@]}" ping >/dev/null 2>&1 \
    || fail "Can't log in to MySQL. If your MySQL user has a password, run: DB_PASSWORD=yourpassword bash run.sh mysql"

  mysql "${MYSQL_ARGS[@]}" -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME:-django} CHARACTER SET utf8mb4;"
else
  unset DB_ENGINE || true
fi

say "Setting up database tables ($([ "$MODE" = mysql ] && echo MySQL || echo SQLite))"
python manage.py migrate --noinput

# 4. Admin login (only created the first time) -------------------------------
python manage.py shell -c "
from django.contrib.auth import get_user_model
U = get_user_model()
if not U.objects.filter(is_superuser=True).exists():
    U.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Created admin login -> username: admin  password: admin')
" 2>/dev/null

# 5. Run ---------------------------------------------------------------------
say "Starting server at http://127.0.0.1:8000  (admin: http://127.0.0.1:8000/admin)  -- press Ctrl+C to stop"
exec python manage.py runserver 127.0.0.1:8000
