from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, HousingAmenities, RoomAmenities


class HousingAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingAmenities
        fields = '__all__'


class RoomAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAmenities
        fields = '__all__'


class HousingSerializer(WritableNestedModelSerializer):
    housing_amenities = HousingAmenitiesSerializer(required=False)
    room_amenities = RoomAmenitiesSerializer(required=False)

    class Meta:
        model = Hotel
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Исключаем поля с типом Boolean, имеющие значение False
        return {key: value for key, value in ret.items() if not isinstance(value, bool) or value}

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