from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from multiselectfield import MultiSelectField
from .constants import DESTINATION_CHOICES, CAR_CATEGORIES, TRANSMISSION_TYPES, STEERING_TYPES, BODY_TYPES, DRIVE_TYPES, \
    FUEL_TYPES, SEATING_CAPACITY, CONDITION_CHOICES, CURRENCY_CHOICES, SAFETY_EQUIPMENT_CHOICES, \
    BRAND_CHOICES, COLOR_CHOICES, AMENITIES_CHOICES, PASSENGER_CAPACITY_CHOICES
from apps.travel.constants import PAYMENT_CHOICES
from apps.users.email import CustomUser


class Transfer(models.Model):
    class Meta:
        verbose_name = 'Трансфер'
        verbose_name_plural = 'Трансферы'

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, verbose_name='Марка автомобиля')
    description = models.TextField(verbose_name='Описание автомобиля', blank=True)
    category = models.CharField(choices=CAR_CATEGORIES, max_length=50, verbose_name='Категория автомобиля')
    body_type = models.CharField(choices=BODY_TYPES, max_length=50, verbose_name='Тип кузова')
    transmission = models.CharField(choices=TRANSMISSION_TYPES, max_length=50, verbose_name='Тип коробки передач')
    steering = models.CharField(choices=STEERING_TYPES, max_length=50, verbose_name='Руль')
    drive_type = models.CharField(choices=DRIVE_TYPES, max_length=50, verbose_name='Тип привода')
    fuel_type = models.CharField(choices=FUEL_TYPES, max_length=50, verbose_name='Тип топлива')
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, verbose_name='Цвет автомобиля')
    passenger = models.CharField(choices=SEATING_CAPACITY, max_length=50, verbose_name='Вместимость пассажиров')
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=50, verbose_name='Состояние автомобиля')
    fuel_consumption = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Расход топлива на 100км')
    minimum_age = models.PositiveIntegerField(verbose_name='Минимальный возраст водителя')
    passenger_capacity = models.IntegerField(choices=PASSENGER_CAPACITY_CHOICES, default=1,
                                             verbose_name="Количество пассажирских мест")
    year = models.PositiveIntegerField(verbose_name='Год выпуска',
                                       validators=[MinValueValidator(1970), MaxValueValidator(2025)])
    driving_experience = models.PositiveIntegerField(verbose_name='Минимальный стаж вождения для аренды')
    amenities = MultiSelectField(choices=AMENITIES_CHOICES, max_length=100, verbose_name="Внутренние удобства")
    safety_equipment = MultiSelectField(choices=SAFETY_EQUIPMENT_CHOICES, max_length=100,
                                        verbose_name='Наличие системы безопасности')
    location = models.CharField(choices=DESTINATION_CHOICES, max_length=50, verbose_name='Область нахождения машины')
    car_address = models.CharField(max_length=255, verbose_name='Адрес')
    pickup_region = MultiSelectField(choices=DESTINATION_CHOICES + (('Все', 'Все'),), max_length=100,
                                     verbose_name='Регион получения')
    check_in_time = models.TimeField(verbose_name="Время заезда")
    check_out_time = models.TimeField(verbose_name="Время отъезда")
    can_arrange_pickup_return = models.BooleanField(default=True,
                                                    verbose_name='Может ли клиент договориться о месте получения/возврата автомобиля')
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, verbose_name='Валюта')
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма аренды (Сутки)')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')

    def __str__(self):
        return self.brand


class TransferImage(models.Model):
    class Meta:
        verbose_name = 'Изображение трансфера'
        verbose_name_plural = 'Изображения тарнсферов'

    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, related_name='transfer_images')
    image = models.ImageField(upload_to='images/car/', null=True, verbose_name="Изображение автомобиля")


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
