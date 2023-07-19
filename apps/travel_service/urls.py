from rest_framework.routers import DefaultRouter
from .views import TravelServiceViewSet


router = DefaultRouter()
router.register('travel-services', TravelServiceViewSet)

urlpatterns = router.urls
