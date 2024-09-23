from django.db import models
from django.utils.crypto import get_random_string

class Snippet(models.Model):
    slug = models.SlugField(unique=True, max_length=50, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_random_string(8)  # Auto-generate a slug if not provided
        super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug
