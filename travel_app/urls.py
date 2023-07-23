from django.contrib import admin
from django.urls import path, include
from .settings.yasg import urlpatterns_swagger as doc_urls
from apps.travel.urls import router as travel_router
from apps.news.urls import router as news_router
from apps.travel_service.urls import router as travel_service_router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.registry.extend(travel_router.registry)
router.registry.extend(news_router.registry)
router.registry.extend(travel_service_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include('apps.travel.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.travel_service.urls')),
    path('', include('apps.news.urls')),
]

urlpatterns += doc_urls