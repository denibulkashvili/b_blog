"""Models for posts app"""
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    """Creates a Post model"""

    title = models.CharField(max_length=200, verbose_name="post_title")
    description = models.TextField(default="", max_length=600)
    content = models.TextField(default="")
    tags = models.ManyToManyField(
        "Tag", related_name="posts" 
    )

    # pylint: disable=missing-docstring
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    """Creates a Tag model"""

    name = models.CharField(max_length=20, verbose_name="tag name")

    def __str__(self):
        return self.name

    # pylint: disable=missing-docstring
    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"pk": self.pk})
