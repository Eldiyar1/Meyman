from rest_framework.routers import DefaultRouter
from .views import TransferViewSet, TransferReservationViewSet, TransfersFavoriteViewSet

router = DefaultRouter()
router.register(r'transfers', TransferViewSet)
router.register(r'transfer_reservations', TransferReservationViewSet)
router.register(r'transfers_favorite', TransfersFavoriteViewSet)

urlpatterns = router.urls
