from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CarReservationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'carreservation', CarReservationViewSet)


urlpatterns = router.urls
