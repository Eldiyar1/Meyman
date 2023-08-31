from rest_framework import serializers
from .models import WishlistAlbum, HouseFavorite
from ..travel.serializers import HousingGetSerializer


class HouseFavoriteSerializer(serializers.ModelSerializer):
    housing = HousingGetSerializer(read_only=True)

    def get_fields(self):
        fields = super().get_fields()
        fields['housing'] = HousingGetSerializer(read_only=True)
        return fields

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
