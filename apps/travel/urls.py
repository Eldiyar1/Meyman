from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, HousingReservationViewSet, RoomViewSet, HousingModelViewSet

router = DefaultRouter()
router.register('housing', HousingModelViewSet)
router.register('housing_reservations', HousingReservationViewSet)
router.register('reviews', ReviewViewSet)
router.register('rooms', RoomViewSet)

urlpatterns = router.urls
