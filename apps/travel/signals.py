from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.advertising.models import Advertising
from apps.news.models import News
from apps.travel.models import HousingImage, RoomImage
from apps.travel_service.models import TransferImage
from apps.users.models import ReviewSite, Profile

MODELS_TO_COMPRESS = [Profile, News, Advertising, TransferImage, HousingImage, RoomImage]


def compress_images(sender, instance, created, **kwargs):
    if created:
        print(f"Compressing image for {instance}")
        instance.compress_image()


for model in MODELS_TO_COMPRESS:
    post_save.connect(compress_images, sender=model)
