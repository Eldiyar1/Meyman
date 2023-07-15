from rest_framework import serializers
from travel.models import TravelService, Hotel, News


class TravelServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelService
        fields = (
            'id',
            'service_name',
            'description',
            'price',
            'location',
            'is_available',
            'formatted_start_date',
            'formatted_end_date'
        )


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            'id',
            'hotel_name',
            'description',
            'daily_price',
            'available_rooms',
            'is_available'
        )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'content',
            'published_date',
            'formatted_published_date',
            'author_fullname_list',
        )
