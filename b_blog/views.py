from django.views.generic import TemplateView
from posts.models import Post, Tag


class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"