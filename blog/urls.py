from django.urls import path
from . import views

urlpatterns = [
    # Empty path for home page
    path("", views.home, name="blog-home"),
]
 