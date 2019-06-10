"""Models for posts app"""
import uuid
from datetime import date
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    """Creates a Post model"""

    title = models.CharField(max_length=200, verbose_name="post title")
    description = models.TextField(default="", max_length=260)
    content = models.TextField(blank=True, default="")
    tags = models.ManyToManyField("Tag", related_name="posts")
    date_created = models.DateField(default=date.today)
    is_featured = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="covers/", default="covers/default.jpg")
    cover_source = models.CharField(max_length=1000, verbose_name="cover image source", default="", blank=True)
    cover_author = models.CharField(max_length=200, verbose_name="cover image author", default="Unknown", blank=True)
    cover_caption = models.CharField(max_length=200, verbose_name="cover image caption", default="Photo", blank=True)
    # cover_thumbnail = ImageSpecField(
    #     source="cover",
    #     processors=[ResizeToFill(240, 180)],
    #     format="JPEG",
    #     options={"quality": 60},
    # )
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    # pylint: disable=missing-docstring
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # pylint:disable=arguments-differ
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)  # Call the real save() method

    class Meta:
        ordering = ["-date_created"]


class Tag(models.Model):
    """Creates a Tag model"""

    name = models.CharField(max_length=20, verbose_name="tag name")
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # pylint:disable=arguments-differ
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)  # Call the real save() method

    # pylint: disable=missing-docstring
    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]
