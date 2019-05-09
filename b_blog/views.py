"""Basic project views"""
from django.views.generic import TemplateView
from posts.models import Post, Tag


class HomePageView(TemplateView):
    """Creates Home page view"""
    template_name = "index.html"


class AboutPageView(TemplateView):
    """Creates About page view"""
    template_name = "about.html"
