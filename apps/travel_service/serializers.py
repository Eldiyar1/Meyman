from rest_framework import serializers
from .models import Search, Transfer, Car
from .constants import DESTINATION_CHOICES, SAFETY_EQUIPMENT_CHOICES


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
            'transfer_location', 'destination_location', 'pickup_date', 'pickup_time', 'return_location',
            'return_date', 'return_time', 'with_driver', 'different_pickup_places'
        )


class CarSerializer(serializers.ModelSerializer):
    pickup_region = serializers.MultipleChoiceField(choices=DESTINATION_CHOICES + (('Все', 'Все'),),
                                                    label="Регион получения")
    return_region = serializers.MultipleChoiceField(choices=DESTINATION_CHOICES + (('Все', 'Все'),),
                                                    label="    Регион возврата")

    has_safety_equipment = serializers.MultipleChoiceField(choices=SAFETY_EQUIPMENT_CHOICES,
                                                           label="Наличие системы безопасности")

    class Meta:
        model = Car
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        operating_area = data.get('operating_area', [])

        if 'Все' in operating_area:
            data['operating_area'] = [choice[0] for choice in DESTINATION_CHOICES if choice[0] != 'Все']

        return data
