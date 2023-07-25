from rest_framework import serializers
from .models import  CarReservation, AccommodationReservation, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'avatar', 'date_joined')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=50,
        write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=50,
        write_only=True
    )
    class Meta:
        model=User 
        fields=('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password' : 'Пароли отличаются'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


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


