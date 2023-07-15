from django.urls import path
from travel.views import *

list_create = {
    'get': 'list',
    'post': 'create'
}

retrieve_update_destroy = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
}

urlpatterns = [
    path('travel-services/', TravelServiceViewSet.as_view(list_create)),
    path('travel-services/<int:pk>/', TravelServiceViewSet.as_view(retrieve_update_destroy)),
    path('hotels/', HotelViewSet.as_view(list_create)),
    path('hotels/<int:pk>/', HotelViewSet.as_view(retrieve_update_destroy)),
    path('news/', NewsViewSet.as_view(list_create)),
    path('news/<int:pk>/', NewsViewSet.as_view(retrieve_update_destroy)),
]