<<<<<<< HEAD
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TravelServiceViewSet, HotelViewSet, NewsViewSet, SignalViewSet

router = DefaultRouter()
router.register(r'travel-services', TravelServiceViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'news', NewsViewSet)
router.register(r'Signal', SignalViewSet, basename='Signal')


=======
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, ApartmentViewSet, HostelViewSet, GuestHouseViewSet, SanatoriumViewSet

router = DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('hostels', HostelViewSet)
router.register('apartment', ApartmentViewSet)
router.register('guest-houses', GuestHouseViewSet)
router.register('sanatoriums', SanatoriumViewSet)
>>>>>>> Eldiyar

urlpatterns = router.urls
