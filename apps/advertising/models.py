from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Реклама"
        verbose_name_plural="Рекламы"

# Пока только базовые данные 