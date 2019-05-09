from django.test import TestCase
from django.urls import reverse

from posts import views
from posts.models import Post, Tag


class HomePageTests(TestCase):
    """Tests home page"""

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")

    def test_home_page_contains_correct_header(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>b_blog")

    def homepage_displays_correct_post_title(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h2>Test</h2>")


class PostListPageTests(TestCase):
    """Test post list view"""

    def setUp(self):
        self.post = Post.objects.create(title="Test")

    def test_post_list_template(self):
        response = self.client.get(reverse("posts:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_list.html")

    def test_post_list_page_renders_posts(self):
        response = self.client.get(reverse("posts:post_list"))
        self.assertContains(response, "Test")


class PostDetailPageTests(TestCase):
    """Test post detail view"""

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(
            title="Hello World!",
            description="Descriptions: Test post",
            content="Content: This is a test post.",
        )

    def setUp(self):
        self.post = Post.objects.get(id=1)

    def test_post_detail_template(self):
        response = self.client.get(f"/posts/id/{self.post.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_detail.html")

    def test_post_detail_page_displays_post_details(self):
        response = self.client.get(f"/posts/id/{self.post.id}/")
        self.assertContains(response, "Hello World")
        self.assertContains(response, "Descriptions: Test post")
        self.assertContains(response, "Content: This is a test post.")

    def test_post_detail_view_displays_list_of_related_tags(self):
        tag1 = Tag.objects.create(name="tag 1")
        tag2 = Tag.objects.create(name="tag 2")
        self.post.tags.add(tag1)
        self.post.tags.add(tag2)
        response = self.client.get(f"/posts/id/{self.post.id}/")
        self.assertContains(response, "tag 1")
        self.assertContains(response, "tag 2")

class TagListPageTests(TestCase):
    """Test tag list view"""

    def setUp(self):
        self.tag = Tag.objects.create(name="test tag")

    def test_tag_list_template(self):
        response = self.client.get(reverse("posts:tag_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/tag_list.html")

    def test_post_list_page_renders_posts(self):
        response = self.client.get(reverse("posts:tag_list"))
        self.assertContains(response, "test tag")


class TagDetailPageTests(TestCase):
    "Test tag detail page"

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="test tag")

    def setUp(self):
        self.tag = Tag.objects.get(id=1)

    def test_tag_detail_template(self):
        response = self.client.get(f"/posts/tags/id/{self.tag.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/tag_detail.html")

    def test_tag_detail_page_displays_tags(self):
        response = self.client.get(f"/posts/tags/id/{self.tag.id}/")
        self.assertContains(response, "test tag")

    def test_tag_detail_view_diplays_related_posts(self):
        self.post1 = Post.objects.create(title="Test related posts - Main post")
        self.post2 = Post.objects.create(title="Test related posts - Secondary post")
        self.post1.tags.add(self.tag)
        self.post2.tags.add(self.tag)
        response = self.client.get(f"/posts/tags/id/{self.tag.id}/")
        self.assertContains(response, "Main post")
        self.assertContains(response, "Secondary post")



class AboutPageTests(TestCase):
    """Tests About page"""

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_home_page_contains_correct_header(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About</h1>")
