from rest_framework import serializers

from .constants import HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES
from .models import Hotel, Hostel, Apartment, GuestHouse, Sanatorium, Housing, Rating, HouseReservation
from ..review.serializers import ReviewSerializer


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class HousingSerializer(serializers.ModelSerializer):
    housing_amenities = serializers.MultipleChoiceField(choices=HOUSING_AMENITIES_CHOICES, label="Комнатные удобства")
    room_amenities = serializers.MultipleChoiceField(choices=ROOM_AMENITIES_CHOICES, label="Жилищные удобства")
    ratings_received = RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Housing
        fields = '__all__'
    def get_average_rating(self, obj):
        reviews = obj.review_hotel.all()
        total_reviews = reviews.count()
        if total_reviews > 0:
            sum_stars = sum(review.stars for review in reviews)
            return round(sum_stars / total_reviews, 2)
        return 0

class HouseReservationSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%d-%m-%Y')
    check_out_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = HouseReservation
        fields = '__all__'


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


class SanatoriumSerializer(HousingSerializer):
    class Meta(HousingSerializer.Meta):
        model = Sanatorium
