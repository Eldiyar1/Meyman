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
            'start_date',
            'end_date',
            'is_available'
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
            'author',
            'published_date',
            'author_fullname_list',
        )
