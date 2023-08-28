from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .constants import USER_TYPE_CHOICES
from .validators import validate_email, validate_password
from .models import CustomUser, Profile, ReviewSite


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        return validate_password(value)

    def validate_email(self, value):
        queryset = CustomUser.objects.all()
        return validate_email(value, queryset)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        # Token.objects.get_or_create(user=user)
        return user


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


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordResetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        style={"input_type": "password"}, help_text="​​From 6 to 20", min_length=6
    )


class PasswordResetCodeSerializer(serializers.Serializer):
    code = serializers.CharField()


class PasswordResetSearchUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email']
