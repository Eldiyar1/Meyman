from rest_framework.routers import DefaultRouter
from .views import HousingViewSet, ReviewViewSet, HousingReservationViewSet, RoomViewSet, \
    HousingAvailabilityViewSet, HousingImageViewSet, RoomsImagesViewSet

router = DefaultRouter()
router.register('housing', HousingViewSet)
router.register('housing_reservations', HousingReservationViewSet)
router.register('reviews', ReviewViewSet)
router.register('rooms', RoomViewSet)
router.register('availability', HousingAvailabilityViewSet)
router.register("housingimage", HousingImageViewSet)
router.register("roomsimages", RoomsImagesViewSet)

urlpatterns = router.urls
