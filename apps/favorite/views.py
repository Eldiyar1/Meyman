from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import WishlistAlbum, HouseFavorite
from .serializers import WishlistAlbumSerializer, HouseFavoriteSerializer


class WishlistAlbumViewSet(viewsets.ModelViewSet):
    queryset = WishlistAlbum.objects.all()
    serializer_class = WishlistAlbumSerializer

class HouseFavoriteViewSet(viewsets.ModelViewSet):
    queryset = HouseFavorite.objects.all()
    serializer_class = HouseFavoriteSerializer
