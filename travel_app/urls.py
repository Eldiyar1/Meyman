from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .settings.yasg import urlpatterns_swagger as doc_urls

urlpatterns = [
          path('admin/', admin.site.urls),
          path('api/users/', include('apps.users.urls')),
          path('api/travel/', include('apps.travel.urls')),
          path('api/travel_sevice/', include('apps.travel_service.urls')),
          path('api/news/', include('apps.news.urls')),
          path('api/weather/', include('apps.weather_forecast.urls')),
          path('api/currency_conversion', include('apps.currency_conversion.urls')),
          path('api/advertising', include('apps.advertising.urls')),
          path('api/favorite/', include('apps.favorite.urls')),
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_urls
