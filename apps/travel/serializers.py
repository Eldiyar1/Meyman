from rest_framework import serializers

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Housing


class HousingSerializer(serializers.ModelSerializer):
    housing_amenities = serializers.MultipleChoiceField(choices=HOUSING_AMENITIES_CHOICES, label="Комнатные удобства")
    room_amenities = serializers.MultipleChoiceField(choices=ROOM_AMENITIES_CHOICES, label="Жилищные удобства")

    class Meta:
        model = Housing
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
