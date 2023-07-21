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
    adults = models.PositiveIntegerField(default=1, verbose_name="Взрослые")
    teens = models.PositiveIntegerField(default=0, verbose_name="Подростки")
    children = models.PositiveIntegerField(default=0, verbose_name="Дети")
    infants = models.PositiveIntegerField(default=0, verbose_name="Младенцы")
    pets = models.PositiveIntegerField(default=0, verbose_name="Домашние животные")

    def formatted_check_in_date_date(self):
        return self.check_in_date.strftime('%d-%m-%Y')

    def formatted_check_out_date_date(self):
        return self.check_out_date.strftime('%d-%m-%Y')


class Transfer(models.Model):
    class Meta:
        verbose_name = "Поиск трансфера"
        verbose_name_plural = "Поиск Трансферов"

    transfer_location = models.CharField(max_length=100, verbose_name="Место получения трансфера")
    pickup_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                   verbose_name="Дата получения трансфера")
    pickup_time = models.TimeField(verbose_name="Время получения трансфера")
    return_location = models.CharField(max_length=100, verbose_name="Место возврата трансфера")
    return_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                   verbose_name="Дата возврата трансфера")
    return_time = models.TimeField(verbose_name="Время возврата трансфера")
    with_driver = models.BooleanField(default=False, verbose_name='Трансфер с водителем')

    def formatted_pickup_date(self):
        return self.pickup_date.strftime('%d-%m-%Y')

    def formatted_return_date(self):
        return self.return_date.strftime('%d-%m-%Y')
