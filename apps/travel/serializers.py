from rest_framework import serializers

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES
from .models import Housing, HousingReview, HousingReservation, Room, RoomImage, HousingImage


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'


class RoomPostSerializer(serializers.ModelSerializer):
    room_amenities = serializers.MultipleChoiceField(choices=ROOM_AMENITIES_CHOICES, label="Удобства")

    class Meta:
        model = Room
        fields = '__all__'


class RoomGetSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True, )

    class Meta:
        model = Room
        fields = ('price_per_night', 'room_images', 'room_amenities', 'num_rooms',  'max_guest_capacity',
                  'room_area', 'single_bed', 'double_bed', 'queen_bed', 'king_bed', 'sofa_bed')


class HousingReviewSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(format='%d-%m-%Y', read_only=True)

    class Meta:
        model = HousingReview
        fields = '__all__'


class HousingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingImage
        fields = '__all__'


class HousingPostSerializer(serializers.ModelSerializer):
    housing_amenities = serializers.MultipleChoiceField(choices=HOUSING_AMENITIES_CHOICES, label="Удобства")

    class Meta:
        model = Housing
        fields = '__all__'


class HousingGetSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    housing_images = HousingImageSerializer(many=True, read_only=True, )
    reviews = HousingReviewSerializer(many=True, read_only=True, label="Отзывы")
    rooms = RoomGetSerializer(many=True, read_only=True)

    class Meta:
        model = Housing
        fields = ('housing_name', 'stars', 'average_rating', 'reviews',
                  'housing_amenities', 'address', 'housing_images',
                  'check_in_time_start', 'check_in_time_end',
                  'check_out_time_start', 'check_out_time_end', 'rooms'
                  )

    def get_average_rating(self, obj):
        reviews = HousingReview.objects.filter(housing=obj)  # Получаем все связанные отзывы
        if reviews:
            total_rating = sum([
                (review.staff_rating +
                 review.comfort_rating +
                 review.cleanliness_rating +
                 review.value_for_money_rating +
                 review.food_rating +
                 review.location_rating) / 6
                for review in reviews
            ])
            average_rating = total_rating / len(reviews)
            return round(average_rating, 1)
        return 0


class HousingReservationSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%d-%m-%Y')
    check_out_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = HousingReservation
        fields = '__all__'
