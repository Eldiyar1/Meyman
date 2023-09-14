from rest_framework import serializers

from .constants import *
from .models import Housing, HousingReview, HousingReservation, Room, RoomImage, HousingImage, HousingAvailability
from .service import get_average_rating, validate_beds, get_cheapest_room_price, get_housing_image, get_room_name, \
    get_price_per_night_convertede


class HousingAvailabilityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingAvailability
        fields = ('rooms', 'housing', 'date', 'is_available')


class HousingAvailabilityGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingAvailability
        fields = ('rooms', 'date', 'is_available')


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ('id', 'image', 'room')


class RoomSerializer(serializers.ModelSerializer):
    bed_type = serializers.MultipleChoiceField(choices=BED_CHOICES, label="Тип кроватей")
    room_amenities = serializers.MultipleChoiceField(choices=ROOM_AMENITIES_CHOICES, label="Удобства в номере")
    kitchen = serializers.MultipleChoiceField(choices=KITCHEN_CHOICES, label="Кухня")
    outside = serializers.MultipleChoiceField(choices=OUTSIDE_CHOICES, label="На улице")
    bathroom = serializers.MultipleChoiceField(choices=BATHROOM_AMENITIES_CHOICES, label="Ванная")

    class Meta:
        model = Room
        fields = ('housing', 'room_name', 'price_per_night', 'room_amenities', 'kitchen', 'outside', 'bathroom',
                  'num_rooms', 'bathroom', 'bedrooms', 'bed_type', 'single_bed', 'double_bed', 'queen_bed', 'king_bed',
                  'sofa_bed', 'max_guest_capacity', 'room_area', 'smoking_allowed', 'Free_cancellation_anytime')
        currency = serializers.ChoiceField(choices=['USD', 'EUR', 'KGS'])

    def validate(self, data):
        validate_beds(data.get('single_bed'), data.get('double_bed'), data.get('queen_bed'),
                      data.get('king_bed'), data.get('sofa_bed'))
        return data


class ConvertedRoomSerializer(RoomSerializer):
    price_per_night_converted = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = RoomSerializer.Meta.fields + ('price_per_night_converted',)

    def get_price_per_night_converted(self, obj):
        return get_price_per_night_convertede(self, obj)


class HousingReviewSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(format='%d-%m-%Y', read_only=True)

    class Meta:
        model = HousingReview
        fields = ('id', 'user', 'housing', 'comment', 'date_added',
                  'cleanliness_rating', 'comfort_rating', 'staff_rating',
                  'value_for_money_rating', 'food_rating', 'location_rating')


class HousingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingImage
        fields = "__all__"


class HousingPostSerializer(serializers.ModelSerializer):
    cheapest_room_price = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField(read_only=True)
    images = HousingImageSerializer(many=True)
    reviews = HousingReviewSerializer(many=True, read_only=True, label="Отзывы")
    rooms = RoomSerializer(many=True, read_only=True, label="Номера")
    breakfast_type = serializers.MultipleChoiceField(choices=BREAKFAST_CHOICES, label="Типы завтрака")
    location = serializers.ReadOnlyField(default="27.3 км от центра")

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        housing = Housing.objects.create(**validated_data)

        image_models = [
            HousingImage(housing=housing, **image)
            for image in images_data]
        HousingImage.objects.bulk_create(image_models)
        return housing

    class Meta:
        model = Housing
        fields = (
            'id', 'user', 'housing_name', 'location', 'images', 'stars', 'average_rating',
            'reviews', 'free_internet', 'bar', 'restaurant', 'airport_transfer', 'gym',
            "children_playground", "region",
            "car_rental", 'paid_transfer', 'park', 'paid_parking', 'spa_services', 'pool', 'paid_bar', 'gym',
            'children_playground', 'car_rental', 'room_service', 'poolside_bar', 'cafe', 'breakfast_type',
            'in_room_internet', 'hotel_wide_internet', 'address', 'check_in_time_start', 'check_in_time_end',
            'check_out_time_start', 'check_out_time_end', 'cheapest_room_price', 'rooms', 'slug')

    def get_cheapest_room_price(self, obj):
        return get_cheapest_room_price(self, obj)

    def get_average_rating(self, obj):
        return get_average_rating(self, obj)


class HousingGetSerializer(serializers.ModelSerializer):
    availability = HousingAvailabilityGetSerializer(many=True, read_only=True)
    cheapest_room_price = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField(read_only=True)
    housing_images = HousingImageSerializer(many=True, read_only=True)
    housing_image = serializers.SerializerMethodField()
    reviews = HousingReviewSerializer(many=True, read_only=True, label="Отзывы")
    rooms = RoomSerializer(many=True, read_only=True, label="Номера")
    breakfast_type = serializers.MultipleChoiceField(choices=BREAKFAST_CHOICES, label="Типы завтрака")
    location = serializers.ReadOnlyField(default="27.3 км от центра")

    class Meta:
        model = Housing
        fields = (
            'id', 'user', 'housing_name', 'location', 'housing_image', 'housing_images', 'stars', 'average_rating',
            'reviews', 'free_internet', 'bar', 'restaurant', 'airport_transfer', 'gym',
            "children_playground", "region",
            "car_rental", 'paid_transfer', 'park', 'paid_parking', 'spa_services', 'pool', 'paid_bar', 'gym',
            'children_playground', 'car_rental', 'room_service', 'poolside_bar', 'cafe', 'breakfast_type',
            'in_room_internet', 'hotel_wide_internet', 'address', 'check_in_time_start', 'check_in_time_end',
            'check_out_time_start', 'check_out_time_end', 'cheapest_room_price', 'rooms', 'availability', 'slug')

    def get_housing_image(self, obj):
        return get_housing_image(self, obj)

    def get_cheapest_room_price(self, obj):
        return get_cheapest_room_price(self, obj)

    def get_average_rating(self, obj):
        return get_average_rating(self, obj)


class HousingReservationSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%d-%m-%Y')
    check_out_date = serializers.DateField(format='%d-%m-%Y')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    room_name = serializers.SerializerMethodField()

    class Meta:
        model = HousingReservation
        fields = ("id", 'user', 'housing', 'check_in_date',
                  'check_out_date', 'username', 'client_email', 'room_name', 'phone_number', 'adults', 'children')

    def get_room_name(self, obj):
        return get_room_name(self, obj)
