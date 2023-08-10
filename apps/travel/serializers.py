from rest_framework import serializers

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES
from .models import Hotel, Hostel, Apartment, Sanatorium, Housing, HousingReview, HousingReservation, \
    Room, House, RoomImage, HousingImage


class HousingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingReview
        fields = '__all__'


class HousingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingImage
        fields = '__all__'


class HousingSerializer(serializers.ModelSerializer):
    housing_amenities = serializers.MultipleChoiceField(choices=HOUSING_AMENITIES_CHOICES, label="Удобства")
    ratings = HousingReviewSerializer(many=True, read_only=True, label="Отзывы")
    average_rating = serializers.SerializerMethodField()
    housing_images = HousingImageSerializer(many=True, read_only=True,)

    class Meta:
        model = Housing
        fields = '__all__'

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HousingReservationSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%d-%m-%Y')
    check_out_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = HousingReservation
        fields = '__all__'


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    room_amenities = serializers.MultipleChoiceField(choices=ROOM_AMENITIES_CHOICES, label="Удобства")
    room_images = RoomImageSerializer(many=True, read_only=True,)

    class Meta:
        model = Room
        fields = '__all__'


class HotelSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = Hotel


class HostelSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = Hostel


class ApartmentSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = Apartment


class HouseSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = House


class SanatoriumSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = Sanatorium
