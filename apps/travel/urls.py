from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TravelServiceViewSet, HotelViewSet, NewsViewSet, SignalViewSet

router = DefaultRouter()
router.register(r'travel-services', TravelServiceViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'news', NewsViewSet)
router.register(r'Signal', SignalViewSet, basename='Signal')



urlpatterns = router.urls
