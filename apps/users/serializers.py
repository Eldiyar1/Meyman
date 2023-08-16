from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
from .models import CustomUser, Profile, ReviewSite

class SignUpSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 8 or len(value) > 20:
            raise ValidationError("Password must be between 8 and 20 characters long.")

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError("Email has already been used")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.get_or_create(user=user)
        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'firstname', 'lastname', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}


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


class ReviewSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSite
        fields = "__all__"
