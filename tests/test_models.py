"""Module to test models"""
from django.test import TestCase
from posts.models import Post, Tag


class PostTestCase(TestCase):
    """Tests Post model"""

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title="Test")  # pylint:disable:no-member

    def setUp(self):
        self.post = Post.objects.get(id=1)

    def test_get_absolute_url(self):
        """Tests get_absolute_url() method"""
        self.assertEqual(self.post.get_absolute_url(), f"/posts/read/{self.post.slug}/")

    def test_title_field(self):
        """Tests title field in Post"""
        field_label = self.post._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "post_title")
        max_length = self.post._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)

    def test_description_field(self):
        """Tests description field in Post"""
        field_label = self.post._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")
        max_length = self.post._meta.get_field("description").max_length
        self.assertEqual(max_length, 600)

    def test_content_field(self):
        """Tests content field in Post"""
        field_label = self.post._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")

    def test_post_tags_field(self):
        """Tests tags field in Post"""
        field_label = self.post._meta.get_field("tags").verbose_name
        self.assertEqual(field_label, "tags")

    def test_post_can_query_tags_through_tags_field(self):
        """Tests if Post can query related tags"""
        tag = Tag.objects.create(name="test tag")
        self.post.tags.add(tag)
        self.assertEqual(self.post.tags.get(id=1), tag)


class TagTestCase(TestCase):
    """Tests Tag model"""

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="test")

    def setUp(self):
        self.tag = Tag.objects.get(id=1)

    def test_name_field(self):
        """Tests name field in Tag"""
        field_label = self.tag._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "tag name")
        max_length = self.tag._meta.get_field("name").max_length
        self.assertEqual(max_length, 20)
