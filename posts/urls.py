"""Urlconf for posts app"""
from django.urls import path
from . import views

# pylint:disable=invalid-name
app_name = "posts"

urlpatterns = [
    path("all", views.PostListView.as_view(), name="post_list"),
    path("read/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("tags/", views.TagListView.as_view(), name="tag_list"),
    path("tag/<slug:slug>/", views.TagDetailView.as_view(), name="tag_detail"),
]
