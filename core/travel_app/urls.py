"""
URL configuration for travel_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.travel.urls import router as travel_router
from apps.news.urls import router as news_router
from apps.travel_service.urls import router as travel_service_router
from apps.currency_conversion.urls import router as currency_conversion_router
from apps.weather_forecast.urls import router as weather_forecast_router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.registry.extend(travel_router.registry)
router.registry.extend(news_router.registry)
router.registry.extend(travel_service_router.registry)
router.registry.extend(currency_conversion_router.registry)
router.registry.extend(weather_forecast_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)