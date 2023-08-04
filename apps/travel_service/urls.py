from rest_framework.routers import DefaultRouter
from .views import TransferViewSet, TransferReservationViewSet, TransferImageViewSet

router = DefaultRouter()
router.register(r'transfers', TransferViewSet)
router.register(r'transfer_reservations', TransferReservationViewSet)
router.register(r'transfer_image', TransferImageViewSet)

urlpatterns = router.urls
