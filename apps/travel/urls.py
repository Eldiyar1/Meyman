from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, ApartmentViewSet, HostelViewSet, GuestHouseViewSet, SanatoriumViewSet, RatingViewSet, \
    HouseReservationViewSet, HousingImageViewSet

router = DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('hostels', HostelViewSet)
router.register('apartments', ApartmentViewSet)
router.register('guest-houses', GuestHouseViewSet)
router.register('sanatoriums', SanatoriumViewSet)
router.register('house_reservations', HouseReservationViewSet)
router.register('ratings', RatingViewSet)
router.register('housing_image', HousingImageViewSet)


urlpatterns = router.urls
