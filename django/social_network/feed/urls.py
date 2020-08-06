from django.urls import path

from . import views

urlpatterns = [
    path("", views.feed, name="feed"),
    path("post", views.post, name="post")
]
