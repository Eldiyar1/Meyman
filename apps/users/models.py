from django.db import models
from django.contrib.auth.models import User

from apps.travel.models import Hotel, TravelService, News


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to='avatars/', blank=True, null=True
    )

class Reservation(models.Model):
    Reserve = models.ForeignKey(
        TravelService, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.id


class Favorite(models.Model):

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    hotel = models.ForeignKey(
        News, on_delete=models.CASCADE, null=True, blank=True,
        related_name='Hotel'
    )
    travel_service = models.ForeignKey(
        TravelService, on_delete=models.CASCADE, null=True, blank=True,
        related_name='Travel_service'
    )
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, null=True, blank=True,
        related_name='News'
    )
