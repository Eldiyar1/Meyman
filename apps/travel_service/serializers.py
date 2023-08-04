from rest_framework import serializers
from .models import Transfer, TransferReservation, TransferImage
from .constants import DESTINATION_CHOICES, SAFETY_EQUIPMENT_CHOICES


class TransferImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferImage
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):
    pickup_region = serializers.MultipleChoiceField(choices=DESTINATION_CHOICES + (('Все', 'Все'),),
                                                    label="Регион получения")
    return_region = serializers.MultipleChoiceField(choices=DESTINATION_CHOICES + (('Все', 'Все'),),
                                                    label="Регион возврата")
    images = serializers.SerializerMethodField(label='Изображение трансфера')
    has_safety_equipment = serializers.MultipleChoiceField(choices=SAFETY_EQUIPMENT_CHOICES,
                                                           label="Наличие системы безопасности")

    class Meta:
        model = Transfer
        fields = '__all__'

    def get_images(self, obj):
        images = obj.transfer_images.all()
        return TransferSerializer(images, many=True).data

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
