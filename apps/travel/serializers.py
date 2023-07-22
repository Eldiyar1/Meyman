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
        fields = '__all__'

class HostelSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = Hostel
        fields = '__all__'

class ApartmentSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = Apartment
        fields = '__all__'


class GuestHouseSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = GuestHouse
        fields = '__all__'

class SanatoriumSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = Sanatorium
        fields = '__all__'




