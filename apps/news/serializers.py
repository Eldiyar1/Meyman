from rest_framework import serializers
from .models import News
from apps.review.models import Review
from apps.review.serializers import ReviewSerializer


class NewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField(read_only=True)
    published_date = serializers.DateTimeField(format='%H:%M:%S, %d-%m-%Y', read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'content', 'published_date', 'link', 'is_favorite', 'reviews', 'average_rating')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        reviews = Review.objects.filter(news=instance)
        data['reviews'] = ReviewSerializer(reviews, many=True).data
        return data

    def get_average_rating(self, obj):
        reviews = obj.review_news.all()
        total_reviews = reviews.count()
        if total_reviews > 0:
            sum_stars = sum(review.stars for review in reviews)
            return round(sum_stars / total_reviews, 2)
        return 0
