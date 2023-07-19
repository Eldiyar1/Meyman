from rest_framework.routers import DefaultRouter
from .views import PriceRangeViewSet, HousingTypeViewSet, AccommodationTypeViewSet, BedTypeViewSet, HotelViewSet, \
    ApartmentViewSet, HostelViewSet, GuestHouseViewSet, TravelServiceViewSet, AuthorViewSet, NewsViewSet

router = DefaultRouter()
router.register(r'price_ranges', PriceRangeViewSet, )
router.register(r'housing_types', HousingTypeViewSet, )
router.register(r'accommodation_types', AccommodationTypeViewSet, )
router.register(r'bed_types', BedTypeViewSet, )
router.register(r'hotels', HotelViewSet)
router.register(r'hostels', HostelViewSet)
router.register(r'apartment', ApartmentViewSet)
router.register(r'guest-houses', GuestHouseViewSet)
router.register(r'travel-services', TravelServiceViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = router.urls
