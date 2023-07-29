from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CarReservationViewSet,AccommodationReservationViewSet,\
    SignUpView, LoginView, OwnerView, ClientView

router = DefaultRouter()
router.register(r'carreservation', CarReservationViewSet)
router.register(r'accommodationreservation', AccommodationReservationViewSet)

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('owner/', OwnerView.as_view(), name='owner'),
    path('client/', ClientView.as_view(), name='client')

]
urlpatterns += router.urls
