"""Module for testing views"""
from django.test import TestCase
from django.urls import reverse
from posts.models import Post, Tag


class HomePageTests(TestCase):
    """Tests home page"""

    def test_home_page_status_code(self):
        """Tests if homepage status code is 200"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Tests if homepage view uses index.html template"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")

    def test_home_page_contains_correct_header(self):
        """Tests if homepage contains b_blog heading"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "b_blog")

    def homepage_displays_correct_post_title(self):
        """Tests if homepage contains title or rendered post"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h2>Test</h2>")


class PostListPageTests(TestCase):
    """Test post list view"""

    def setUp(self):
        self.post = Post.objects.create(title="Test")

    def test_post_list_template(self):
        """Tests if post list view status code and correct template used"""
        response = self.client.get(reverse("posts:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_list.html")

    def test_post_list_page_renders_posts(self):
        """Tests if post list view renders correct post"""
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
        """Tests post detail view status code and template"""
        response = self.client.get(f"/posts/read/{self.post.slug}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/post_detail.html")

    def test_post_detail_page_displays_post_details(self):
        """Tests if post detail view renders correct post details"""
        response = self.client.get(f"/posts/read/{self.post.slug}/")
        self.assertContains(response, "Hello World")
        self.assertContains(response, "Descriptions: Test post")
        self.assertContains(response, "Content: This is a test post.")

    def test_post_detail_view_displays_list_of_related_tags(self):
        """Tests if post detail view renders correct related tags"""
        tag1 = Tag.objects.create(name="tag 1")
        tag2 = Tag.objects.create(name="tag 2")
        self.post.tags.add(tag1)
        self.post.tags.add(tag2)
        response = self.client.get(f"/posts/read/{self.post.slug}/")
        self.assertContains(response, "tag 1")
        self.assertContains(response, "tag 2")


class TagListPageTests(TestCase):
    """Test tag list view"""

    def setUp(self):
        self.tag = Tag.objects.create(name="test tag")

    def test_tag_list_template(self):
        """Tests if tag list view status code and correct template used"""
        response = self.client.get(reverse("posts:tag_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/tag_list.html")

    def test_tag_list_page_renders_tags(self):
        """Tests if tag list view renders correct tag"""
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
        """Tests tag detail view status code and template"""
        response = self.client.get(f"/posts/tag/{self.tag.slug}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/tag_detail.html")

    def test_tag_detail_page_displays_tags(self):
        """Tests if tag detail view renders correct tag name"""
        response = self.client.get(f"/posts/tag/{self.tag.slug}/")
        self.assertContains(response, "test tag")

    def test_tag_detail_view_diplays_related_posts(self):
        """Tests if tag detail view renders list of related posts"""
        post1 = Post.objects.create(title="Test related posts - Main post")
        post2 = Post.objects.create(title="Test related posts - Secondary post")
        post1.tags.add(self.tag)
        post2.tags.add(self.tag)
        response = self.client.get(f"/posts/tag/{self.tag.slug}/")
        self.assertContains(response, "Main post")
        self.assertContains(response, "Secondary post")


class AboutPageTests(TestCase):
    """Tests About page"""

    def test_view_uses_correct_template(self):
        """Tests if about view renders correct template"""
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_home_page_contains_correct_header(self):
        """Tests if about page contains About header"""
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About</h1>")
