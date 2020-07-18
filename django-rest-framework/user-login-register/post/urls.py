from django.urls import path, include
from rest_framework.routers import DefaultRouter

from post import views

router = DefaultRouter()
router.register("me", views.MyPostViewSet)
router.register("", views.PostViewSet)


app_name = "post"

urlpatterns = [
    path("", include(router.urls))
]
