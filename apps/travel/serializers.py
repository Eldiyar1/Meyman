from rest_framework import serializers

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES, MAX_IMAGES
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Housing, Rating, HouseReservation, HousingImage


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class HousingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingImage
        fields = '__all__'


class HousingSerializer(serializers.ModelSerializer):
    housing_amenities = serializers.MultipleChoiceField(choices=HOUSING_AMENITIES_CHOICES, label="Комнатные удобства")
    room_amenities = serializers.MultipleChoiceField(choices=ROOM_AMENITIES_CHOICES, label="Жилищные удобства")
    ratings_received = RatingSerializer(many=True, read_only=True, label="Рейтинги")
    images = serializers.SerializerMethodField(label="Изображение жилья")

    class Meta:
        model = Housing
        fields = '__all__'

    def get_images(self, obj):
        images = obj.housing_images.all()
        return HousingImageSerializer(images, many=True).data


class HouseReservationSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%d-%m-%Y')
    check_out_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = HouseReservation
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


class GuestHouseSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = GuestHouse


class SanatoriumSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = Sanatorium
