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
    safety_equipment = serializers.MultipleChoiceField(choices=SAFETY_EQUIPMENT_CHOICES,
                                                       label="Система безопасности")
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

    def get_average_rating(self, obj):
        reviews = TransferReview.objects.filter(transfer=obj)
        total_rating = sum([
            (review.comfortable_driving +
             review.technical_condition +
             review.cleanliness_level +
             review.price_quality_ratio +
             review.safety_level +
             review.how_it_went) / 6
            for review in reviews
        ])
        if reviews:
            average_rating = total_rating / len(reviews)
            return round(average_rating, 1)
        return 0

class TransferReservationSerializer(serializers.ModelSerializer):
    pickup_date = serializers.DateField(format='%d-%m-%Y')
    return_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = TransferReservation
        fields = '__all__'
