from .models import CarReservation, AccommodationReservation,CustomUser, Profile
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
from rest_framework import serializers


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            password = validated_data.pop("password")

            user = super().create(validated_data)

            user.set_password(password)

            user.save()

            token, created = Token.objects.get_or_create(user=user)

            return user
        

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)

        if user and user.is_active:
            tokens = create_jwt_pair_for_user(user)
            data['access_token'] = tokens['access']
            data['refresh_token'] = tokens['refresh']
        else:
            raise serializers.ValidationError('Invalid email or password')

        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'email', 'phone_number']



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

