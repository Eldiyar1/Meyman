from rest_framework import serializers
from .models import Transfer, TransferReservation
from .constants import DESTINATION_CHOICES, SAFETY_EQUIPMENT_CHOICES


class TransferSerializer(serializers.ModelSerializer):
    operating_area = serializers.MultipleChoiceField(choices=DESTINATION_CHOICES + (('Все', 'Все'),),
                                                    label="Территории эксплуатации")
    safety_equipment = serializers.MultipleChoiceField(choices=SAFETY_EQUIPMENT_CHOICES, label="Система безопасности")

    class Meta:
        model = Transfer
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        operating_area = data.get('operating_area', [])

        if 'Все' in operating_area:
            data['operating_area'] = [choice[0] for choice in DESTINATION_CHOICES if choice[0] != 'Все']

        return data

class TransferReservationSerializer(serializers.ModelSerializer):
    pickup_date = serializers.DateField(format='%d-%m-%Y')
    return_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = TransferReservation
        fields = '__all__'
