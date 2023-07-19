from rest_framework import serializers
from .models import PriceRange, HousingType, AccommodationType, BedType, TravelService, Hotel, Hostel, Apartment, \
    GuestHouse, News, Author


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


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ('id', 'accommodation_name', 'image', 'description', 'daily_price', 'available_rooms', 'is_available',
                  'price_range', 'housing_type', 'accommodation_type', 'bed_type')


class HotelSerializer(AccommodationSerializer):
    class Meta(AccommodationSerializer.Meta):
        model = Hotel


class HostelSerializer(AccommodationSerializer):
    class Meta(AccommodationSerializer.Meta):
        model = Hostel


class ApartmentSerializer(AccommodationSerializer):
    class Meta(AccommodationSerializer.Meta):
        model = Apartment


class GuestHouseSerializer(AccommodationSerializer):
    class Meta(AccommodationSerializer.Meta):
        model = GuestHouse


class TravelServiceSerializer(serializers.ModelSerializer):
    start_date = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TravelService.objects.all())
    end_date = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TravelService.objects.all())

    class Meta:
        model = TravelService
        fields = ('id', 'service_name', 'image', 'description', 'price', 'location', 'is_available', 'start_date',
                  'end_date', 'formatted_start_date', 'formatted_end_date')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'fullname')


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Author.objects.all())

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'content', 'formatted_published_date', 'author', 'author_fullname_list',
                  'link')


class CurrencyConverterSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    currency = serializers.ChoiceField(choices=['USD', 'EUR', 'RUB', 'KZT'])
