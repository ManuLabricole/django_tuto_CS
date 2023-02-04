from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    # Empty path for home page
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("about/", views.about, name="blog-about"),
]
 