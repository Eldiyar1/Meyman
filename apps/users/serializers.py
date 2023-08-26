from rest_framework.authtoken.models import Token
from rest_framework import serializers

from .validators import validate_email, validate_password
from .models import CustomUser, Profile, ReviewSite


class SignUpSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return validate_password(value)

    def validate_email(self, value):
        queryset = CustomUser.objects.all()
        return validate_email(value, queryset)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.get_or_create(user=user)
        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    verify_code = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'email', 'phone_number']


class ReviewSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSite
        fields = "__all__"