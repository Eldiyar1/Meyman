from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from PIL import Image
from multiselectfield import MultiSelectField
from .constants import DESTINATION_CHOICES, CAR_CATEGORIES, TRANSMISSION_TYPES, STEERING_TYPES, BODY_TYPES, DRIVE_TYPES, \
    FUEL_TYPES, SEATING_CAPACITY, CONDITION_CHOICES, CURRENCY_CHOICES, SAFETY_EQUIPMENT_CHOICES, \
    BRAND_CHOICES, COLOR_CHOICES, AMENITIES_CHOICES, PASSENGER_SITS_CHOICES
from apps.users.email import CustomUser


class Transfer(models.Model):
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, verbose_name='Марка трансфера')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    category = models.CharField(choices=CAR_CATEGORIES, max_length=50, verbose_name='Категория')
    body_type = models.CharField(choices=BODY_TYPES, max_length=50, verbose_name='Тип кузова')
    transmission = models.CharField(choices=TRANSMISSION_TYPES, max_length=50, verbose_name='Тип коробки передач')
    steering = models.CharField(choices=STEERING_TYPES, max_length=50, verbose_name='Руль')
    drive_type = models.CharField(choices=DRIVE_TYPES, max_length=50, verbose_name='Тип привода')
    fuel_type = models.CharField(choices=FUEL_TYPES, max_length=50, verbose_name='Тип топлива')
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, verbose_name='Цвет')
    passenger = models.CharField(choices=SEATING_CAPACITY, max_length=50, verbose_name='Вместимость пассажиров')
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=50, verbose_name='Состояние автомобиля')
    fuel_consumption = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Расход топлива на 100км')
    minimum_age = models.PositiveIntegerField(verbose_name='Минимальный возраст водителя')
    passenger_sits = models.IntegerField(choices=PASSENGER_SITS_CHOICES, default=1, verbose_name="Пассажирских мест")
    year = models.PositiveIntegerField(verbose_name='Год выпуска',
                                       validators=[MinValueValidator(1970), MaxValueValidator(2025)])
    driving_experience = models.PositiveIntegerField(verbose_name='Минимальный стаж вождения для аренды')
    amenities = MultiSelectField(choices=AMENITIES_CHOICES, max_length=150, verbose_name="Внутренние удобства")
    safety_equipment = MultiSelectField(choices=SAFETY_EQUIPMENT_CHOICES, max_length=255,
                                        verbose_name='Наличие системы безопасности')
    pickup_location = models.CharField(choices=DESTINATION_CHOICES, max_length=100, verbose_name='Место получения')
    car_address = models.CharField(max_length=255, verbose_name='Адрес получения')
    return_location = models.CharField(choices=DESTINATION_CHOICES, max_length=100, verbose_name='Место возврата')
    check_in_time = models.TimeField(verbose_name="Время заезда")
    check_out_time = models.TimeField(verbose_name="Время отъезда")
    can_arrange_pickup_return = models.BooleanField(default=True,
                                                    verbose_name='Может ли клиент договориться о месте получения/возврата автомобиля')
    operating_area = MultiSelectField(choices=DESTINATION_CHOICES + (('По всему КР', 'По всему КР'),), max_length=100,
                                      verbose_name='Территории эксплуатации')
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=25, verbose_name='Валюта')
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма аренды (Сутки)')

    def __str__(self):
        return self.brand

    def save(self, *args, **kwargs):
        if 'По всему КР' in self.operating_area:
            self.operating_area = [choice[0] for choice in DESTINATION_CHOICES if choice[0] != 'По всему КР']
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Трансфер'
        verbose_name_plural = 'Трансферы'


class TransferImage(models.Model):
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, related_name='transfer_images')
    transfer_image = models.ImageField(upload_to='transfers', verbose_name="Изображения Трансфера")

    def __str__(self):
        return f"Image for {self.transfer.brand}"

    def compress_image(self):
        img = Image.open(self.transfer_image.path)
        img = img.convert('RGB')
        img.thumbnail((800, 800))
        img.save(self.transfer_image.path, 'JPEG', quality=90)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.compress_image()

    class Meta:
        verbose_name = 'Изображение трансфера'
        verbose_name_plural = 'Изображения трансферов'


class TransferReservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, verbose_name="Трансфер")
    transfer_location = models.CharField(max_length=255, verbose_name="Место получения трансфера")
    destination_location = models.CharField(max_length=255, verbose_name="Куда вы хотите поехать")
    pickup_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                   verbose_name="Дата получения трансфера")
    return_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                   verbose_name="Дата возврата трансфера")
    pickup_time = models.TimeField(verbose_name="Время получения трансфера")
    return_time = models.TimeField(verbose_name="Время возврата трансфера")
    return_location = models.CharField(max_length=255, verbose_name="Место возврата трансфера")
    different_pickup_places = models.BooleanField(default=False, verbose_name='Разные места получения')
    with_driver = models.BooleanField(default=False, verbose_name='Трансфер с водителем')

    def __str__(self):
        return f"Бронь трансфера для {self.user} на {self.pickup_date}"

    class Meta:
        verbose_name = "Бронь трансфера"
        verbose_name_plural = "Бронь Трансферов"


class TransferReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, verbose_name='Название трансфера',
                                 related_name='reviews')
    comment = models.TextField(max_length=500, blank=True, null=True, verbose_name='Комментарий')
    date_added = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"Отзыв от {self.user} на {self.transfer}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
