from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import WishlistAlbum, HouseFavorite
from .serializers import WishlistAlbumSerializer, HouseFavoriteSerializer
from .permissions import IsrMineOrReadOnly
from .filters import WishlistFilters


class WishlistAlbumViewSet(viewsets.ModelViewSet):
    queryset = WishlistAlbum.objects.all()
    serializer_class = WishlistAlbumSerializer
    permission_classes = [IsrMineOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = WishlistFilters

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return WishlistAlbum.objects.filter(user=self.request.user)


class HouseFavoriteViewSet(viewsets.ModelViewSet):
    queryset = HouseFavorite.objects.all()
    serializer_class = HouseFavoriteSerializer
    permission_classes = [IsrMineOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return HouseFavorite.objects.filter(user=self.request.user)
