from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.travel.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.travel_service.urls')),
    path('', include('apps.news.urls')),
]
urlpatterns += doc_urls
