from rest_framework import serializers
from .models import WishlistAlbum, HouseFavorite


class HouseFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseFavorite
        fields = ('id',
                  'wishlist_album', 'housing')


class WishlistAlbumSerializer(serializers.ModelSerializer):
    houseFavorite = HouseFavoriteSerializer(many=True, read_only=True)

    class Meta:
        model = WishlistAlbum
        fields = ('id',
                  'user', 'title', 'houseFavorite',)
