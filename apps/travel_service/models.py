from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from .constants import DESTINATION_CHOICES, CAR_CATEGORIES, TRANSMISSION_TYPES, STEERING_TYPES, BODY_TYPES, DRIVE_TYPES, \
    FUEL_TYPES, SEATING_CAPACITY, CONDITION_CHOICES, CURRENCY_CHOICES, MINIMUM_AGE_CHOICES
from apps.users.constants import PAYMENT_CHOICES
from multiselectfield import MultiSelectField


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


class Car(models.Model):
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

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
    brand = models.CharField(max_length=50, verbose_name='Марка автомобиля')
    model = models.CharField(max_length=50, verbose_name='Модель автомобиля')
    color = models.CharField(max_length=50, verbose_name='Цвет автомобиля', blank=True)
    year = models.PositiveIntegerField(verbose_name='Год выпуска автомобиля')
    description = models.TextField(verbose_name='Описание автомобиля', blank=True)
    fuel_consumption = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Расход топлива на 100км')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')
    operating_area = MultiSelectField(choices=DESTINATION_CHOICES + (('Все', 'Все'),), max_length=50,
                                      verbose_name='Территория эксплуатации')
    has_fire_extinguisher = models.BooleanField(verbose_name='Наличие огнетушителя', default=False)
    has_first_aid_kit = models.BooleanField(verbose_name='Наличие аптечки', default=False)
    has_spare_wheel = models.BooleanField(verbose_name='Наличие запасного колеса', default=False)
    has_airbags = models.BooleanField(verbose_name='Наличие подушка безопасности', default=False)
    has_emergency_tools = models.BooleanField(verbose_name='Наличие инструментов аварийной ситуации', default=False)
    has_dashboard_camera = models.BooleanField(verbose_name='Наличие авторегистратора', default=False)
    check_in_time = models.TimeField(verbose_name="Время заезда")
    check_out_time = models.TimeField(verbose_name="Время отъезда")
