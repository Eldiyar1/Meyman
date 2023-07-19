from rest_framework import serializers
from .models import Advertising
from django.utils.text import slugify

class AdvertisingSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Advertising
        fields = '__all__'

    def create(self, validated_data):
        if not validated_data.get('slug'):
            title = validated_data.get('title')
            slug = slugify(title)

            queryset = Advertising.objects.filter(slug=slug)
            if queryset.exists():
                slug = f"{slug}-{queryset.count() + 1}"

            validated_data['slug'] = slug

        return super().create(validated_data)