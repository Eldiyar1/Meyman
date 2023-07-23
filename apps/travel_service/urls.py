from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SearchViewSet, TransferViewSet

router = DefaultRouter()
router.register(r'search', SearchViewSet)
router.register(r'transfer', TransferViewSet)

urlpatterns = router.urls
