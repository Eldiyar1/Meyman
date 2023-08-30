from rest_framework import serializers
from .models import WishlistAlbum, HouseFavorite


class WishlistAlbumSerializer(serializers.ModelSerializer):
    favorite = serializers.ReadOnlyField()
    class Meta:
        model = WishlistAlbum
        fields = ('id',
                  'user', 'title', 'favorite')


class HouseFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseFavorite
        fields = ('id',
                  'user', 'wishlist_album', 'housing', 'transfer')
