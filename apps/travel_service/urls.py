
from rest_framework.routers import DefaultRouter
from .views import SearchViewSet, TransferViewSet, CarViewSet

router = DefaultRouter()
router.register(r'search', SearchViewSet)
router.register(r'transfer', TransferViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = router.urls
