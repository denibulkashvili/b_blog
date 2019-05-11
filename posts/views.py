"""Views module for posts app"""
from django.views.generic import ListView, DetailView
from .models import Post, Tag

# Create your views here.
class PostListView(ListView):  # pylint: disable=too-many-ancestors
    """Creates post list view"""

    model = Post
    template_name = "posts/post_list.html"


class PostDetailView(DetailView):  # pylint: disable=too-many-ancestors
    """Create post detail view"""

    model = Post
    template_name = "posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        return context


class TagListView(ListView):  # pylint:disable=too-many-ancestors
    """Creates tag list view"""

    model = Tag
    template_name = "posts/tag_list.html"


class TagDetailView(DetailView):  # pylint:disable=too-many-ancestors
    """Creates tag detail view"""

    model = Tag
    template_name = "posts/tag_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context["posts"] = self.object.posts.all()
        return context
