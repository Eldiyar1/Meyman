from rest_framework.routers import DefaultRouter
from .views import PriceRangeViewSet, HousingTypeViewSet, AccommodationTypeViewSet, BedTypeViewSet, HotelViewSet, \
    ApartmentViewSet, HostelViewSet, GuestHouseViewSet

router = DefaultRouter()
router.register('price_ranges', PriceRangeViewSet)
router.register('housing_types', HousingTypeViewSet)
router.register('accommodation_types', AccommodationTypeViewSet)
router.register('bed_types', BedTypeViewSet)
router.register('hotels', HotelViewSet)
router.register('hostels', HostelViewSet)
router.register('apartment', ApartmentViewSet)
router.register('guest-houses', GuestHouseViewSet)

urlpatterns = router.urls
