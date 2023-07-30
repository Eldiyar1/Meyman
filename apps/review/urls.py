from rest_framework.routers import DefaultRouter

from apps.review.views import ReviewViewSet

router = DefaultRouter()
router.register(r'review', ReviewViewSet)

urlpatterns = router.urls
