from django.db import models
from django.utils.text import slugify

from apps.travel.service import compress_image


class Advertising(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    text = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='ad_images/',
        verbose_name="Изображение"
    )
    link = models.URLField(
        verbose_name="Ссылка на рекламадателя"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="человеко-понятный url",
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

        if self.image:
            self.compress_image()

    def compress_image(self):
        return compress_image(self)

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"
