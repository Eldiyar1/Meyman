from rest_framework.routers import DefaultRouter
from .views import HousingViewSet, ReviewViewSet, HousingReservationViewSet, RoomViewSet, History_reservationsViewSet, \
    HousingAvailabilityViewSet

router = DefaultRouter()
router.register('housing', HousingViewSet)
router.register('housing_reservations', HousingReservationViewSet)
router.register('reviews', ReviewViewSet)
router.register('rooms', RoomViewSet)
router.register('history_reservations', History_reservationsViewSet)
router.register('availability', HousingAvailabilityViewSet)

urlpatterns = router.urls

