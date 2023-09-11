from django.db.models.signals import post_save

from apps.news.models import News
from apps.travel.models import HousingImage, RoomImage
from apps.travel_service.models import TransferImage
from apps.users.models import Profile

MODELS_TO_COMPRESS = [News, Profile, TransferImage, HousingImage, RoomImage]


def compress_images(sender, instance, created, **kwargs):
    if created:
        instance.compress_image()

    for model in MODELS_TO_COMPRESS:
        post_save.connect(compress_images, sender=model)
