from apps.travel.models import HousingReview


def get_average_rating(self, obj):
    reviews = HousingReview.objects.filter(housing=obj)
    if reviews:
        total_rating = sum([
            (review.staff_rating +
             review.comfort_rating +
             review.cleanliness_rating +
             review.value_for_money_rating +
             review.food_rating +
             review.location_rating) / 6
            for review in reviews
        ])
        average_rating = total_rating / len(reviews)
        return round(average_rating, 1)
    return 0
def compress_image(self):
    img = Image.open(self.room_image.path)
    img = img.convert('RGB')
    img.thumbnail((800, 800))
    img.save(self.room_image.path, 'JPEG', quality=90)