from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Housing


class HousingSerializer(WritableNestedModelSerializer):
    housing_amenities = serializers.MultipleChoiceField(choices=HOUSING_AMENITIES_CHOICES, label="Комнатные удобства")
    room_amenities = serializers.MultipleChoiceField(choices=ROOM_AMENITIES_CHOICES, label="Жилищные удобства")

    class Meta:
        model = Housing
        fields = '__all__'

    def get_stars(self, obj):
        num_stars = min(obj.stars, 5)
        return '*' * num_stars


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
