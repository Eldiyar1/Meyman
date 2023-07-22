from rest_framework.routers import DefaultRouter

from .views import HotelViewSet, ApartmentViewSet, HostelViewSet, GuestHouseViewSet, SanatoriumViewSet

router = DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('hostels', HostelViewSet)
router.register('apartment', ApartmentViewSet)
router.register('guest-houses', GuestHouseViewSet)
router.register('sanatoriums', SanatoriumViewSet)

urlpatterns = router.urls
