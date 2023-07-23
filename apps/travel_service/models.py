from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

DESTINATION_CHOICES = (
    ('Бишкек', 'Бишкек'),
    ('Джалал-Абад', 'Джалал-Абад'),
    ('Иссык-Куль', 'Иссык-Куль'),
    ('Ош', 'Ош'),
    ('Нарын', 'Нарын'),
    ('Талас', 'Талас'),
    ('Баткен', 'Баткен'),
)


class Search(models.Model):
    class Meta:
        verbose_name = "Поиск жилья"
        verbose_name_plural = "Поиск жилья"

    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES, verbose_name="Куда")
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Заезд")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Выезд")
    adults = models.PositiveIntegerField(default=1, verbose_name="Взрослые(от 18 лет)")
    teens = models.PositiveIntegerField(default=0, verbose_name="Подростки(от 13-18 лет)")
    children = models.PositiveIntegerField(default=0, verbose_name="Дети(от 2-12 лет)")
    infants = models.PositiveIntegerField(default=0, verbose_name="Младенцы(младше 2)")
    pets = models.PositiveIntegerField(default=0, verbose_name="Домашние животные")


class Transfer(models.Model):
    class Meta:
        verbose_name = "Поиск трансфера"
        verbose_name_plural = "Поиск Трансферов"

    transfer_location = models.CharField(max_length=255, verbose_name="Место получения трансфера")
    destination_location = models.CharField(max_length=255, verbose_name="Куда вы хотите поехать")
    pickup_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                   verbose_name="Дата получения трансфера")
    pickup_time = models.TimeField(verbose_name="Время получения трансфера")
    return_location = models.CharField(max_length=255, verbose_name="Место возврата трансфера")
    return_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                   verbose_name="Дата возврата трансфера")
    return_time = models.TimeField(verbose_name="Время возврата трансфера")
    different_pickup_places = models.BooleanField(default=False, verbose_name='Разные места получения')
    with_driver = models.BooleanField(default=False, verbose_name='Трансфер с водителем')
