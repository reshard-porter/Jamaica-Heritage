from django.http import Http404
from django.shortcuts import render

from . import media
from .content import TOPICS, TOPICS_BY_SLUG


def _with_media(topic):
    """Return a copy of a topic with its hero photo and section photos/videos attached."""
    topic_media = media.TOPIC_MEDIA.get(topic['slug'], {})
    section_media = topic_media.get('sections', {})
    return {
        **topic,
        'hero': topic_media.get('hero'),
        'sections': [
            {**section, **section_media.get(section['heading'], {})}
            for section in topic['sections']
        ],
    }


def index(request):
    context = {
        'title': 'Jamaican Culture & Heritage',
        'topics': [_with_media(topic) for topic in TOPICS],
        'home': media.HOME,
    }
    return render(request, 'heritage/index.html', context)


def topic(request, slug):
    page = TOPICS_BY_SLUG.get(slug)
    if page is None:
        raise Http404('No such heritage page')

    position = TOPICS.index(page)
    context = {
        'title': page['title'],
        'page': _with_media(page),
        'previous_page': TOPICS[position - 1] if position > 0 else None,
        'next_page': TOPICS[position + 1] if position < len(TOPICS) - 1 else None,
    }
    return render(request, 'heritage/topic.html', context)
