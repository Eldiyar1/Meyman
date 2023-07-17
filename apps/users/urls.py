from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ReservationViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'reservation', ReservationViewSet)
router.register(r'favorite', FavoriteViewSet)

urlpatterns = router.urls
