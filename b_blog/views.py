"""Basic project views"""
from django.views.generic import TemplateView, ListView
from posts.models import Post


class HomePageView(ListView):
    """Creates Home page view"""
    model = Post
    template_name = "index.html"

class AboutPageView(TemplateView):
    """Creates About page view"""

    template_name = "about.html"
