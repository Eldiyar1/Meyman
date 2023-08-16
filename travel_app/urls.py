from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.travel.urls import router as travel_router
from apps.news.urls import router as news_router
from apps.travel_service.urls import router as travel_service_router
from apps.weather_forecast.urls import router as weather_router
from apps.users.urls import router as users_router
from apps.currency_conversion.urls import router as currency_conversion_router
from apps.advertising.urls import router as advertising_router
from .settings.yasg import urlpatterns_swagger as doc_urls

routers = [
    travel_router,
    news_router,
    travel_service_router,
    weather_router,
    users_router,
    currency_conversion_router,
    advertising_router,
]

router = DefaultRouter()
for rtr in routers:
    router.registry.extend(rtr.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/travel/', include('apps.travel.urls')),
    path('api/travel_service/', include('apps.travel_service.urls')),
    path('api/news/', include('apps.news.urls')),
    path('api/weather/', include('apps.weather_forecast.urls')),
    path('api/currency_conversion/', include('apps.currency_conversion.urls')),
    path('api/advertising/', include('apps.advertising.urls')),
    path('api/favorite/', include('apps.favorite.urls')),
] + router.urls + doc_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

