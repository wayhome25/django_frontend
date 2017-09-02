from django_extensions.db.models import TimeStampedModel

from django.db import models


class Post(TimeStampedModel):
    title = models.CharField(max_length=180)
    content = models.TextField()


class Comment(TimeStampedModel):
    post = models.ForeignKey('Post')
    message = models.TextField()
