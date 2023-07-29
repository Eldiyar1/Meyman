from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CarReservationViewSet,AccommodationReservationViewSet, SignUpView, LoginView

router = DefaultRouter()
router.register(r'carreservation', CarReservationViewSet)
router.register(r'accommodationreservation', AccommodationReservationViewSet)

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')

]
urlpatterns += router.urls
