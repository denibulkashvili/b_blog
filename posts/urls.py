"""Urlconf for posts app"""
from django.urls import path
from . import views

# pylint:disable=invalid-name
app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("<pk>/", views.PostDetailView.as_view(), name="post_detail"),
]
