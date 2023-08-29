from rest_framework import serializers
from apps.travel.models import Room

class CurrencyConversionSerializer(serializers.Serializer):
    currency_1 = serializers.ChoiceField(choices=["USD", "EUR", "KGS"])
    currency_2 = serializers.ChoiceField(choices=["USD", "EUR", "KGS"])
    amount = serializers.FloatField(min_value=0)  





