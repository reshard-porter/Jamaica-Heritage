from .content import TOPICS


def heritage_nav(request):
    """Makes the list of heritage pages available to every template (for the nav bar)."""
    return {'nav_topics': TOPICS}
