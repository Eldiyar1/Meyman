from rest_framework import serializers
from .models import WishlistAlbum, HouseFavorite
from ..travel.service import get_housing_image_for_favorite


class HouseFavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    housing_image = serializers.SerializerMethodField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        housing_representation = {
            "housing_name": instance.housing.housing_name,
            "address": instance.housing.address,
            "region": instance.housing.region,
            "stars": instance.housing.stars,
            "housing_type": instance.housing.housing_type,
            "accommodation_type": instance.housing.accommodation_type,
            "food_type": instance.housing.food_type,
            "free_internet": instance.housing.free_internet,
            "restaurant": instance.housing.restaurant,
            "airport_transfer": instance.housing.airport_transfer,
            "paid_transfer": instance.housing.paid_transfer,
            "gym": instance.housing.gym,
            "children_playground": instance.housing.children_playground,
            "car_rental": instance.housing.car_rental,
            "park": instance.housing.park,
            "paid_parking": instance.housing.paid_parking,
            "spa_services": instance.housing.spa_services,
            "bar": instance.housing.bar,
            "paid_bar": instance.housing.paid_bar,
            "pool": instance.housing.pool,
            "room_service": instance.housing.room_service,
            "poolside_bar": instance.housing.poolside_bar,
            "cafe": instance.housing.cafe,
            "in_room_internet": instance.housing.in_room_internet,
            "hotel_wide_internet": instance.housing.hotel_wide_internet,
            "check_in_time_start": instance.housing.check_in_time_start,
            "check_in_time_end": instance.housing.check_in_time_end,
            "check_out_time_start": instance.housing.check_out_time_start,
            "check_out_time_end": instance.housing.check_out_time_end,
            "children_allowed": instance.housing.children_allowed,
            "pets_allowed": instance.housing.pets_allowed,
            "pet_fee": instance.housing.pet_fee,
            "breakfast_offered": instance.housing.breakfast_offered,
            "breakfast_included": instance.housing.breakfast_included,
            "breakfast_cost_usd": instance.housing.breakfast_cost_usd,
            "breakfast_type": instance.housing.breakfast_type,
            "parking_location": instance.housing.parking_location,
        }
        representation.update(housing_representation)
        return representation

    def get_housing_image(self, obj):
        return get_housing_image_for_favorite(self,obj)

    class Meta:
        model = HouseFavorite
        fields = ('id', 'user', 'wishlist_album', 'housing', 'housing_image')


class WishlistAlbumSerializer(serializers.ModelSerializer):
    houseFavorite = HouseFavoriteSerializer(many=True, read_only=True)
    favorite_count = serializers.SerializerMethodField()

    def get_favorite_count(self, obj):
        return obj.houseFavorite.count()

    class Meta:
        model = WishlistAlbum
        fields = ('id', 'user', 'title', 'favorite_count', 'houseFavorite',)
