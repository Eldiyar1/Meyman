from django.db import models
from django.utils.text import slugify

from apps.travel.models import Housing


class Advertising(models.Model):
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, verbose_name="Место жительства")
    added = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"
