from rest_framework import serializers
from .models import TravelService


class TravelServiceSerializer(serializers.ModelSerializer):
    start_date = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TravelService.objects.all())
    end_date = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TravelService.objects.all())

    class Meta:
        model = TravelService
        fields = ('id', 'service_name', 'image', 'description', 'price', 'location', 'is_available', 'start_date',
                  'end_date', 'formatted_start_date', 'formatted_end_date')
