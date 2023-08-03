from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CarReservationViewSet, AccommodationReservationViewSet, SignUpView, LoginView, AdminReviewViewSet, \
    AdminReviewDetailViewSet, ProfileViewSet, OwnerView, ClientView

router = DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'carreservation', CarReservationViewSet)
router.register(r'accommodationreservation', AccommodationReservationViewSet)
router.register(r'adminreview', AdminReviewViewSet)
router.register(r'admindetailreview', AdminReviewDetailViewSet)
urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('owner/', OwnerView.as_view(), name='owner'),
    path('client/', ClientView.as_view(), name='client')

]
urlpatterns += router.urls
