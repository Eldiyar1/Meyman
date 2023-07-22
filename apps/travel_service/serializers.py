from rest_framework import serializers
from .models import Search, Transfer

class SearchSerializer(serializers.ModelSerializer):
    check_in_date = serializers.DateField(format='%d-%m-%Y')
    check_out_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Search
        fields = (
            'destination', 'check_in_date', 'check_out_date', 'adults',
            'teens', 'children', 'infants', 'pets',
        )

class TransferSerializer(serializers.ModelSerializer):
    pickup_date = serializers.DateField(format='%d-%m-%Y')
    return_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Transfer
        fields = (
            'transfer_location', 'pickup_date', 'pickup_time', 'return_location',
            'return_date', 'return_time', 'with_driver'
        )