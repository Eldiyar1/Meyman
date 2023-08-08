from django.core.validators import MinLengthValidator
from rest_framework import serializers

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Housing, Rating, HouseReservation, HousingImage, \
    Room, RoomImage


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class HousingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingImage
        fields = '__all__'


class HousingSerializer(serializers.ModelSerializer):
    housing_amenities = serializers.MultipleChoiceField(choices=HOUSING_AMENITIES_CHOICES, label="Жилищные удобства")
    ratings_received = RatingSerializer(many=True, read_only=True, label="Рейтинги")
    housing_images = HousingImageSerializer(many=True, read_only=True, label="Изображение жилья")
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True, validators=[MinLengthValidator(5)])

    class Meta:
        model = Housing
        fields = '__all__'

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        housing = Housing.objects.create(**validated_data)
        for image in uploaded_images:
            HousingImage.objects.create(housing=housing, image=image)

        return housing


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    room_amenities = serializers.MultipleChoiceField(choices=ROOM_AMENITIES_CHOICES, label="Удобства номера")
    room_images = RoomImageSerializer(many=True, read_only=True, label="Изображение номера")
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True, validators=[MinLengthValidator(5)])

    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        room = Room.objects.create(**validated_data)
        for image in uploaded_images:
            RoomImage.objects.create(room=room, image=image)

        return room


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
