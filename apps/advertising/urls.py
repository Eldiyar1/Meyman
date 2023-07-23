from django.urls import path, include
from .views import AdvertisingAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("advertising", AdvertisingAPI, basename="advertising")

urlpatterns = router.urls
