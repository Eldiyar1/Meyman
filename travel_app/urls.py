from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .settings.yasg import urlpatterns_swagger as doc_urls

router = DefaultRouter()

urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/users/', include('apps.users.urls')),
      path('api/favorite/', include('apps.favorite.urls')),
      path('api/housing/', include('apps.travel.urls')),
      path('api/travel_service/', include('apps.travel_service.urls')),
      path('api/advertising/', include('apps.advertising.urls')),
      ] + router.urls + doc_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
