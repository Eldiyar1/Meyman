from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, ApartmentViewSet, HostelViewSet, HouseViewSet, SanatoriumViewSet, ReviewViewSet, \
    HousingReservationViewSet, RoomViewSet

router = DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('hostels', HostelViewSet)
router.register('apartments', ApartmentViewSet)
router.register('houses', HouseViewSet)
router.register('sanatoriums', SanatoriumViewSet)
router.register('housing_reservations', HousingReservationViewSet)
router.register('reviews', ReviewViewSet)
router.register('rooms', RoomViewSet)

urlpatterns = router.urls
