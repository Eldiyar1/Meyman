from django.db import models
from apps.users.email import CustomUser
from apps.travel.models import Housing
from apps.travel_service.models import Transfer
from apps.news.models import News

class WishlistAlbum(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Альбом желаний"
        verbose_name_plural = "Альбомы желаний"


    def __str__(self):
        return self.title


class HouseFavorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    wishlist_album = models.ForeignKey(WishlistAlbum, on_delete=models.SET_NULL, blank=True, null=True)
    news = models.OneToOneField(News, on_delete=models.CASCADE, blank=True, null=True)
    housing = models.OneToOneField(Housing, on_delete=models.CASCADE, blank=True, null=True)
    transfer = models.OneToOneField(Transfer, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"