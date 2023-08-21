from rest_framework import serializers
from apps.travel.models import Room

class CurrencyConverterSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    currency = serializers.ChoiceField(choices=['USD', 'EUR', 'RUB', 'KZT'])





