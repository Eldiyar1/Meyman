from rest_framework import serializers
from .models import WishlistAlbum, HouseFavorite

class WishlistAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistAlbum
        fields = '__all__'

class HouseFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseFavorite
        fields = '__all__'
