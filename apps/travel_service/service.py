from apps.travel_service.constants import DESTINATION_CHOICES


def get_average_rating(self, obj):
    from apps.travel_service.models import TransferReview
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