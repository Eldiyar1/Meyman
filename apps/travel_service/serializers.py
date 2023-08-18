from rest_framework import serializers
from .models import Transfer, TransferReservation, TransferReview, TransferImage
from .constants import DESTINATION_CHOICES, SAFETY_EQUIPMENT_CHOICES


class TransferReviewSerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(format='%d-%m-%Y', read_only=True)
    class Meta:
        model = TransferReview
        fields = '__all__'

class TransferImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferImage
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):
    operating_area = serializers.MultipleChoiceField(choices=DESTINATION_CHOICES + (('Все', 'Все'),),
                                                     label="Территории эксплуатации")
    safety_equipment = serializers.MultipleChoiceField(choices=SAFETY_EQUIPMENT_CHOICES, label="Система безопасности")
    transfer_images = TransferImageSerializer(many=True, read_only=True, )
    reviews = TransferReviewSerializer(many=True, read_only=True, label="Отзывы")

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
