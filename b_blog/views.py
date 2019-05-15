"""Main views module"""
from django.views.generic import TemplateView, ListView
from posts.models import Post


class HomePageView(ListView):  # pylint:disable=too-many-ancestors
    """Creates Home page view"""

    model = Post
    template_name = "index.html"


class AboutPageView(TemplateView):
    """Creates About page view"""

    template_name = "about.html"
