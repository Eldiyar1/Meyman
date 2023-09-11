from django.db import models
from apps.users.email import CustomUser
from apps.travel.models import Housing


class HouseFavorite(models.Model):
    wishlist_album = models.ForeignKey("WishlistAlbum", on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='houseFavorite')
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='housing')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"


class WishlistAlbum(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Альбом желаний"
        verbose_name_plural = "Альбомы желаний"

    def __str__(self):
        return self.title
