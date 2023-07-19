from rest_framework import serializers
from .models import News, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'fullname')


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Author.objects.all())

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'content', 'formatted_published_date', 'author', 'link',
                  'author_fullname_list',)
