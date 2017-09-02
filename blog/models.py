from django_extensions.db.models import TimeStampedModel

from django.db import models
from django.urls import reverse


class Post(TimeStampedModel):
    title = models.CharField(max_length=180)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

class Comment(TimeStampedModel):
    post = models.ForeignKey('Post')
    message = models.TextField()
