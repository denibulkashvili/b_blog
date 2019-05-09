"""Views module for posts app"""
from django.views.generic import ListView, DetailView
from .models import Post, Tag

# Create your views here.
class PostListView(ListView): # pylint: disable=too-many-ancestors
    """Creates post list view"""

    model = Post
    template_name = "posts/post_list.html"


class PostDetailView(DetailView): # pylint: disable=too-many-ancestors
    """Create post detail view"""

    model = Post
    template_name = "posts/post_detail.html"
