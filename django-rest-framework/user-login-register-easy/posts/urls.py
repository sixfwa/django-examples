from .views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", PostViewSet, base_name="posts")
urlpatterns = router.urls
