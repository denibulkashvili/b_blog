from django.test import TestCase
from django.urls import reverse

from posts import views
from posts.models import Post, Tag

class HomePageTests(TestCase):
    """Tests home page"""
    def setUp(self):
        self.post = Post.objects.create(title="Test")

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
    pass

class PostDetailPageTests(TestCase):
    pass

class TagListPageTests(TestCase):
    pass

class AboutPageTests(TestCase):
    """Tests About page"""
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_home_page_contains_correct_header(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About</h1>")