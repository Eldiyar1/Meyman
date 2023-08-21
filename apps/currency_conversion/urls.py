from rest_framework.routers import DefaultRouter
from .views import CurrencyConverterViewSet

router = DefaultRouter()
router.register(r'currency-conversion', CurrencyConverterViewSet, basename='currency_conversion')

urlpatterns = router.urls
