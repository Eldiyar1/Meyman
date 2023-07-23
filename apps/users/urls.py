from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, CarReservationViewSet, AccommodationReservationViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'carreservation', CarReservationViewSet)
router.register(r'accommodationreservation', AccommodationReservationViewSet)

urlpatterns = router.urls
