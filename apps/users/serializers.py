from .models import  CarReservation, AccommodationReservation, User, CustomUser
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):

        email_exists = CustomUser.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        token, created = Token.objects.get_or_create(user=user)

        return user


class CurrentUserPostsSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True, view_name="post_detail", read_only=True, source='post_set'
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "posts"]

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


