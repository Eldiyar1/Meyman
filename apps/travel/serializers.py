from rest_framework import serializers

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES
from .models import Housing, HousingReview, HousingReservation, Room, RoomImage, HousingImage, HousingAvailability
from .service import get_average_rating


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ('id', 'image', 'room')


class RoomPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('housing', 'room_name', 'price_per_night', 'room_amenities', 'kitchen', 'amenities', 'num_rooms',
                  'bathroom', 'bedrooms', 'bed_type', 'single_bed', 'double_bed', 'queen_bed', 'king_bed',
                  'sofa_bed', 'max_guest_capacity', 'room_area', 'smoking_allowed')


class RoomGetSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'price_per_night', 'room_images', 'room_amenities', 'num_rooms', 'max_guest_capacity',
                  'room_area', 'bed_type')


class HousingAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingAvailability
        fields = ('housing', 'date', 'is_available')


class HousingReviewSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(format='%d-%m-%Y', read_only=True)

    class Meta:
        model = HousingReview
        fields = (
        'id', 'user', 'housing', 'comment', 'date_added', 'cleanliness_rating', 'comfort_rating', 'staff_rating',
        'value_for_money_rating', 'food_rating', 'location_rating')


class HousingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingImage
        fields = ('id', 'image', 'housing')


class HousingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = (
            'housing_name', 'stars', 'address', 'check_in_time_start', 'check_in_time_end',
            'check_out_time_start', 'check_out_time_end', 'free_internet', 'restaurant', 'airport_transfer',
            'paid_transfer', 'park', 'paid_parking', 'spa_services', 'bar', 'paid_bar',
            'pool', 'room_service', 'poolside_bar', 'cafe', 'in_room_internet', 'hotel_wide_internet',
            'children_allowed', 'pets_allowed', 'pet_fee', 'breakfast_offered',
            'breakfast_included', 'breakfast_cost_usd', 'breakfast_type', 'parking_location', 'slug')


class HousingGetSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField(read_only=True)
    housing_images = HousingImageSerializer(many=True, read_only=True)
    reviews = HousingReviewSerializer(many=True, read_only=True, label="Отзывы")
    rooms = RoomGetSerializer(many=True, read_only=True)

    class Meta:
        model = Housing
        fields = ('id',
                  'housing_name', 'stars', 'average_rating', 'reviews', 'free_internet', 'restaurant',
                  'airport_transfer',
                  'paid_transfer', 'park', 'paid_parking', 'spa_services', 'bar', 'paid_bar',
                  'pool', 'room_service', 'poolside_bar', 'cafe', 'in_room_internet', 'hotel_wide_internet',
                  'address', 'housing_images', 'check_in_time_start', 'check_in_time_end',
                  'check_out_time_start', 'check_out_time_end', 'rooms')

    def get_average_rating(self, obj):
        return get_average_rating(obj, obj)


class HousingReservationSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%d-%m-%Y')
    check_out_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = HousingReservation
        fields = ("id", 'user', 'housing', 'destination', 'check_in_date', 'check_out_date', 'adults',
                  'teens', 'children', 'infants', 'pets')
