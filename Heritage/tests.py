from django.test import TestCase
from django.urls import reverse

from .content import TOPICS


class HeritagePageTests(TestCase):
    def test_index_lists_every_topic(self):
        response = self.client.get(reverse('heritage:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jamaican Culture &amp; Heritage')
        for topic in TOPICS:
            self.assertContains(response, reverse('heritage:topic', args=[topic['slug']]))

    def test_every_topic_page_renders(self):
        for topic in TOPICS:
            with self.subTest(topic=topic['slug']):
                response = self.client.get(reverse('heritage:topic', args=[topic['slug']]))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, topic['tagline'])
                for section in topic['sections']:
                    self.assertContains(response, section['heading'])

    def test_unknown_topic_is_404(self):
        response = self.client.get('/heritage/not-a-page/')
        self.assertEqual(response.status_code, 404)

    def test_nav_appears_on_posts_pages_too(self):
        response = self.client.get(reverse('posts:index'))
        self.assertContains(response, reverse('heritage:topic', args=['music']))

    def test_flag_shown_on_symbols_page(self):
        response = self.client.get(reverse('heritage:topic', args=['symbols']))
        self.assertContains(response, 'aria-label="Flag of Jamaica"')

    def test_sections_without_entries_render_no_empty_cards(self):
        # Regression: a section with no "entries" must not loop over dict.items().
        response = self.client.get(reverse('heritage:topic', args=['symbols']))
        self.assertNotContains(response, '<h4></h4>', html=True)


class HeritageMediaTests(TestCase):
    def test_every_media_section_heading_exists(self):
        # A typo in a heading in media.py would silently drop a photo or video.
        from .content import TOPICS_BY_SLUG
        from .media import TOPIC_MEDIA
        for slug, topic_media in TOPIC_MEDIA.items():
            self.assertIn(slug, TOPICS_BY_SLUG)
            headings = {s['heading'] for s in TOPICS_BY_SLUG[slug]['sections']}
            for heading in topic_media.get('sections', {}):
                with self.subTest(slug=slug, heading=heading):
                    self.assertIn(heading, headings)

    def test_every_topic_has_a_hero_photo(self):
        from .media import TOPIC_MEDIA
        for topic in TOPICS:
            with self.subTest(topic=topic['slug']):
                self.assertIn('hero', TOPIC_MEDIA[topic['slug']])

    def test_video_ids_look_valid(self):
        import re
        from . import media
        videos = [v for v in vars(media).values() if isinstance(v, dict) and 'watch_url' in v]
        self.assertGreaterEqual(len(videos), 6)
        for v in videos:
            self.assertRegex(v['id'], r'^[A-Za-z0-9_-]{11}$')

    def test_home_shows_hero_gallery_and_video(self):
        response = self.client.get(reverse('heritage:index'))
        self.assertContains(response, 'images.unsplash.com', count=None)
        self.assertContains(response, 'class="gallery"')
        self.assertContains(response, 'data-video-id="olYYISLYLiU"')

    def test_music_page_has_photos_credits_and_videos(self):
        response = self.client.get(reverse('heritage:topic', args=['music']))
        self.assertContains(response, 'data-video-id="IN0KkGeEURw"')
        self.assertContains(response, 'Bill Fairs')
        self.assertContains(response, 'unsplash.com/photos/')


class YouTubeEmbedTests(TestCase):
    def test_referrer_policy_allows_youtube_embeds(self):
        # 'same-origin' (Django's default) makes YouTube show "Error 153".
        response = self.client.get(reverse('heritage:index'))
        self.assertEqual(response['Referrer-Policy'], 'strict-origin-when-cross-origin')
