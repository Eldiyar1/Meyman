from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, HousingAmenities, RoomAmenities, Housing


class HousingAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingAmenities
        exclude = ('housing',)


class RoomAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAmenities
        exclude = ('housing',)


class HousingSerializer(WritableNestedModelSerializer):
    housing_amenities = HousingAmenitiesSerializer(required=False)
    room_amenities = RoomAmenitiesSerializer(required=False)

    class Meta:
        model = Housing
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['housing_amenities'] is not None:
            data['housing_amenities'] = {k: v for k, v in data['housing_amenities'].items() if v is not False}
        if data['room_amenities'] is not None:
            data['room_amenities'] = {key: value for key, value in data['room_amenities'].items() if value is not False}
        return data

    def get_stars(self, obj):
        return '*' * obj.stars


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

