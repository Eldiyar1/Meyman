from rest_framework import serializers
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, HousingAmenities, RoomAmenities


class HousingAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingAmenities
        exclude = ('housing', )


class RoomAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAmenities
        exclude = ('housing', )


class HousingSerializer(serializers.ModelSerializer):
    housing_amenities = HousingAmenitiesSerializer()
    room_amenities = RoomAmenitiesSerializer()

    class Meta:
        abstract = True
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

