from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, CarReservationViewSet, AccommodationReservationViewSet, AdminReviewViewSet, \
    AdminReviewDetailViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'carreservation', CarReservationViewSet)
router.register(r'accommodationreservation', AccommodationReservationViewSet)
router.register(r'adminreview', AdminReviewViewSet)
router.register(r'admindetailreview', AdminReviewDetailViewSet)

urlpatterns = router.urls
