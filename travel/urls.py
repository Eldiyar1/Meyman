from rest_framework.routers import DefaultRouter
from travel.views import TravelServiceViewSet, HotelViewSet, NewsViewSet

router = DefaultRouter()
router.register(r'travel-services', TravelServiceViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = router.urls

