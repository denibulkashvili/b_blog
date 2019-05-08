from django.test import TestCase
from posts.models import Post, Tag

class PostTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title="Test")

    def setUp(self):
        self.post = Post.objects.get(id=1)

    def test_get_absolute_url(self):
        self.assertEquals(self.post.get_absolute_url(), "post/test/")

    def test_title_field(self):
        field_label = self.post._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")
        max_length = self.post._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    def test_description_field(self):
        field_label = self.post._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")
        max_length = self.post._meta.get_field("description").max_length
        self.assertEqual(max_length, 600)

    def test_content_field(self):
        field_label = self.post._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")


class TagTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(title="test")

    def setUp(self):
        self.tag = Tag.objects.get(id=1)

    def test_name_field(self):
        field_label = self.tag._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "name")
        max_length = self.tag._meta.get_field("title").max_length
        self.assertEqual(max_length, 20)