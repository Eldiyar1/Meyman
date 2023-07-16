from rest_framework import serializers
from travel.models import TravelService, Hotel, News, Author


class TravelServiceSerializer(serializers.ModelSerializer):
    start_date = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TravelService.objects.all())
    end_date = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TravelService.objects.all())

    class Meta:
        model = TravelService
        fields = ('id', 'service_name', 'description', 'price', 'location', 'is_available', 'start_date', 'end_date',
                  'formatted_start_date', 'formatted_end_date')


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'hotel_name', 'description', 'daily_price', 'available_rooms', 'is_available')


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Author.objects.all())

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'formatted_published_date', 'author', 'author_fullname_list')
