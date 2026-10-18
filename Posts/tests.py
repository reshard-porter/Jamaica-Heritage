from django.test import TestCase
from django.urls import reverse

from .models import Posts


class PostsViewTests(TestCase):
    def setUp(self):
        self.post = Posts.objects.create(title='Hello', body='First line\nSecond line')

    def test_root_redirects_to_index(self):
        response = self.client.get('/')
        self.assertRedirects(response, reverse('heritage:index'))

    def test_index_lists_posts(self):
        response = self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Latest Updates')
        self.assertContains(response, reverse('posts:details', args=[self.post.id]))

    def test_index_empty(self):
        Posts.objects.all().delete()
        response = self.client.get(reverse('posts:index'))
        self.assertContains(response, 'No posts yet')

    def test_details_shows_post(self):
        response = self.client.get(reverse('posts:details', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<strong>Hello</strong>', html=True)
        self.assertContains(response, 'Second line')

    def test_details_missing_post_is_404(self):
        response = self.client.get(reverse('posts:details', args=[9999]))
        self.assertEqual(response.status_code, 404)
