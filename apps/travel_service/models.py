from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from multiselectfield import MultiSelectField
from .constants import DESTINATION_CHOICES, CAR_CATEGORIES, TRANSMISSION_TYPES, STEERING_TYPES, BODY_TYPES, DRIVE_TYPES, \
    FUEL_TYPES, SEATING_CAPACITY, CONDITION_CHOICES, CURRENCY_CHOICES, MINIMUM_AGE_CHOICES, SAFETY_EQUIPMENT_CHOICES, \
    BRAND_CHOICES, COLOR_CHOICES, YES_OR_NO, AMENITIES_CHOICES
from apps.travel.constants import PAYMENT_CHOICES
from apps.users.email import CustomUser


class Transfer(models.Model):
    class Meta:
        verbose_name = 'Трансфер'
        verbose_name_plural = 'Трансферы'

    car_location = models.CharField(choices=DESTINATION_CHOICES, max_length=50,
                                    verbose_name='Область нахождения машины')
    image = models.ImageField(upload_to='images/car/', verbose_name="Изображение автомобиля")
    category = models.CharField(choices=CAR_CATEGORIES, max_length=255, verbose_name='Категория автомобиля')
    transmission = models.CharField(choices=TRANSMISSION_TYPES, max_length=255, verbose_name='Тип коробки передач')
    steering = models.CharField(choices=STEERING_TYPES, max_length=50, verbose_name='Руль')
    body_type = models.CharField(choices=BODY_TYPES, max_length=255, verbose_name='Тип кузова')
    drive_type = models.CharField(choices=DRIVE_TYPES, max_length=255, verbose_name='Тип привода')
    fuel_type = models.CharField(choices=FUEL_TYPES, max_length=255, verbose_name='Тип топлива')
    passenger_capacity = models.CharField(choices=SEATING_CAPACITY, max_length=255,
                                          verbose_name='Вместимость пассажиров')
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=255, verbose_name='Состояние автомобиля')
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, verbose_name='Валюта')
    minimum_age = models.CharField(choices=MINIMUM_AGE_CHOICES, max_length=2, verbose_name='Минимальный возраст')
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма аренды (Сутки)')
    car_address = models.CharField(max_length=255, verbose_name='Адрес')
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, verbose_name='Марка автомобиля')
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, verbose_name='Цвет автомобиля', blank=True)
    year = models.PositiveIntegerField(verbose_name='Год выпуска автомобиля', validators=[
        MinValueValidator(1900), MaxValueValidator(2030)])
    description = models.TextField(verbose_name='Описание автомобиля', blank=True)
    fuel_consumption = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Расход топлива на 100км')
    driving_experience = models.PositiveIntegerField(verbose_name='Минимальный стаж вождения для аренды')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')
    pickup_region = MultiSelectField(choices=DESTINATION_CHOICES + (('Все', 'Все'),), max_length=100,
                                     verbose_name='Регион получения')
    return_region = MultiSelectField(choices=DESTINATION_CHOICES + (('Все', 'Все'),), max_length=100,
                                     verbose_name='Регион возврата')
    has_safety_equipment = MultiSelectField(choices=SAFETY_EQUIPMENT_CHOICES, max_length=100,
                                            verbose_name='Наличие системы безопасности')
    amenities = MultiSelectField(choices=AMENITIES_CHOICES, max_length=100, verbose_name="Внутренние удобства")
    check_in_time = models.TimeField(verbose_name="Время заезда")
    check_out_time = models.TimeField(verbose_name="Время отъезда")
    can_arrange_pickup_return = models.CharField(choices=YES_OR_NO, max_length=10,
                                    verbose_name='Может ли клиент договориться о месте получения/возврата автомобиля')

    def __str__(self):
        return self.brand


class TransferReservation(models.Model):
    class Meta:
        verbose_name = "Бронь трансфера"
        verbose_name_plural = "Бронь Трансферов"

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
    transfer = models.OneToOneField(Transfer, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name="Трансфер")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")



class TransfersFavorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Transfer, on_delete=models.CASCADE)


