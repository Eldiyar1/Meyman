from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class TravelService(models.Model):
    class Meta:
        verbose_name = "Туристический сервис"
        verbose_name_plural = "Туристические сервисы"

    service_name = models.CharField(max_length=255, verbose_name="Название сервиса")
    image = models.ImageField(upload_to='images/travel/', verbose_name="Изображение туристического сервиса")
    description = models.TextField(verbose_name="Описание сервиса")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Цена")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    start_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Дата начала")
    end_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Дата окончания")
    is_available = models.BooleanField(default=True, verbose_name='Доступность')

    def __str__(self):
        return self.service_name

    def formatted_start_date(self):
        return self.start_date.strftime('%d-%m-%Y')

    def formatted_end_date(self):
        return self.end_date.strftime('%d-%m-%Y')