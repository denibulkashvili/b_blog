"""Views module for posts app"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Tag

# Create your views here.
class PostListView(ListView):
    """Creates post list view"""
    model = Post
    template_name = "post_list.html"