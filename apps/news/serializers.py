from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    published_date = serializers.DateTimeField(format='%H:%M:%S, %d-%m-%Y', read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'content', 'author_fullname', 'published_date', 'link', 'is_favorite')
