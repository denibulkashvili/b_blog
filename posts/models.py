"""Models for posts app"""
from django.db import models
from django.urls import reverse
from datetime import date
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    """Creates a Post model"""

    title = models.CharField(max_length=200, verbose_name="post_title")
    description = models.TextField(default="", max_length=600)
    content = models.TextField(blank=True, default="")
    tags = models.ManyToManyField(
        "Tag", related_name="posts" 
    )
    date_created = models.DateField(default=date.today)
    is_featured = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="covers/", default="covers/default.jpg")
    cover_thumbnail = ImageSpecField(source='cover',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    

    # pylint: disable=missing-docstring
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        ordering = ["-date_created"]


class Tag(models.Model):
    """Creates a Tag model"""

    name = models.CharField(max_length=20, verbose_name="tag name")

    def __str__(self):
        return self.name

    # pylint: disable=missing-docstring
    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["name"]
