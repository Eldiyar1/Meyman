from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import WishlistAlbum, HouseFavorite
from .serializers import WishlistAlbumSerializer, HouseFavoriteSerializer
from .permissions import IsClientUserOrReadOnly


class WishlistAlbumViewSet(viewsets.ModelViewSet):
    queryset = WishlistAlbum.objects.all()
    serializer_class = WishlistAlbumSerializer
    permission_classes = [IsClientUserOrReadOnly]

class HouseFavoriteViewSet(viewsets.ModelViewSet):
    queryset = HouseFavorite.objects.all()
    serializer_class = HouseFavoriteSerializer
    permission_classes = [IsClientUserOrReadOnly]
