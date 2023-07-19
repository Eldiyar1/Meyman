from rest_framework import serializers
from .models import PriceRange, HousingType, AccommodationType, BedType, Hotel, Hostel, Apartment, GuestHouse


class PriceRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceRange
        fields = ('min_price', 'max_price')


class HousingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingType
        fields = ('id', 'housing_type')


class AccommodationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = ('id', 'accommodation_type',)


class BedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedType
        fields = ('id', 'bed_type')


class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ('id', 'housing_name', 'image', 'description', 'daily_price', 'available_rooms', 'is_available',
                  'price_range', 'housing_type', 'accommodation_type', 'bed_type')


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


class CurrencyConverterSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    currency = serializers.ChoiceField(choices=['USD', 'EUR', 'RUB', 'KZT'])
