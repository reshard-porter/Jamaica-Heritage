from django.db import models
from django.utils import timezone


class Posts(models.Model):
    """A simple blog post."""

    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
