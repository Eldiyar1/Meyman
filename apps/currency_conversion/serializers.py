from rest_framework import serializers

class CurrencyConverterSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    currency = serializers.ChoiceField(choices=['USD', 'EUR', 'RUB', 'KZT'])