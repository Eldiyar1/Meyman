from rest_framework import serializers
from .models import Profile, CarReservation, AccommodationReservation, AdminReview


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CarReservationSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%d-%m-%Y')
    check_out_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = CarReservation
        fields = '__all__'


class AccommodationReservationSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%d-%m-%Y')
    check_out_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = AccommodationReservation
        fields = '__all__'


class AdminReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminReview
        fields = '__all__'
