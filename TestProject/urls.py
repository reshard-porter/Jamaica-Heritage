from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='heritage:index', permanent=False)),
    path('admin/', admin.site.urls),
    path('heritage/', include('Heritage.urls')),
    path('Posts/', include('Posts.urls')),
]
