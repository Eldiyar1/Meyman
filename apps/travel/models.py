from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from django.utils import timezone
from apps.travel.constants import HOUSING_CHOICES, ACCOMMODATION_CHOICES, BEDROOM_CHOICES, BED_CHOICES, \
    FOOD_CHOICES, PARKING_CHOICES, HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES, STAR_CHOICES, PAYMENT_CHOICES, \
    RATING_CHOICES, PARKING_LOCATION_CHOICES
from apps.travel_service.constants import DESTINATION_CHOICES, YES_OR_NO
from django.utils.text import slugify
from apps.users.email import CustomUser


class Housing(models.Model):
    class Meta:
        verbose_name = "Жильё"
        verbose_name_plural = "Жильё"

    housing_name = models.CharField(max_length=255, verbose_name="Название места жительства")
    image = models.ImageField(upload_to='images/housing/', verbose_name="Изображение места жительства")
    description = models.TextField(verbose_name="Описание места жительства")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена за ночь")
    bathrooms = models.PositiveIntegerField(verbose_name='Количество ванн', default=1)
    beds = models.PositiveIntegerField(verbose_name='Количество кроватей', default=1)
    location = models.CharField(max_length=255, verbose_name="местоположение жилища")
    check_in_time_start = models.TimeField(verbose_name="Заезд С")
    check_in_time_end = models.TimeField(verbose_name="Заезд До")
    check_out_time_start = models.TimeField(verbose_name="Отъезд С")
    check_out_time_end = models.TimeField(verbose_name="Отъезд До")
    region = models.CharField(max_length=255, choices=DESTINATION_CHOICES, verbose_name="Область")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    stars = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                        choices=STAR_CHOICES, verbose_name='Количество звезд')
    housing_type = models.CharField(max_length=255, choices=HOUSING_CHOICES, verbose_name="Тип жилья")
    accommodation_type = models.CharField(max_length=255, choices=ACCOMMODATION_CHOICES, verbose_name="Тип размещения")
    bedrooms = models.CharField(max_length=255, choices=BEDROOM_CHOICES, default="Не включено",
                                verbose_name="Количество спален")
    bed_type = models.CharField(max_length=255, choices=BED_CHOICES, verbose_name="Тип кроватей")
    food_type = models.CharField(max_length=255, choices=FOOD_CHOICES, default="Не включено",
                                 verbose_name="Тип питания")
    parking_service = models.CharField(max_length=10, choices=PARKING_CHOICES, default='no',
                                       verbose_name='Услуги парковки')
    parking_cost_usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                           verbose_name='Стоимость парковки в US$ (за день)')
    parking_location = models.CharField(max_length=50, choices=PARKING_LOCATION_CHOICES, blank=True, null=True,
                                        verbose_name='Где находится парковка?')
    housing_amenities = MultiSelectField(choices=HOUSING_AMENITIES_CHOICES, max_length=255,
                                         verbose_name='Удобства в объекте')
    room_amenities = MultiSelectField(choices=ROOM_AMENITIES_CHOICES, max_length=255,
                                      verbose_name='Удобства в номере')
    without_credit_card = models.CharField(choices=YES_OR_NO, default=True, max_length=25,
                                           verbose_name="Без банковской карты")
    free_cancellation = models.CharField(choices=YES_OR_NO, default=False, max_length=25,
                                         verbose_name="Бесплатная отмена")
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default="К оплате сейчас",
                                    verbose_name="Оплата")

    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="человеко-понятный url",
        blank=True, null=True
    )

    def __str__(self):
        return self.housing_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.housing_name)
        super().save(*args, **kwargs)


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='ratings_given')
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='ratings_received')
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, default='0')


class HouseReservation(models.Model):
    class Meta:
        verbose_name = "Бронь жилья"
        verbose_name_plural = "Бронь жилья"

    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES, verbose_name="Куда")
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Заезд")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Выезд")
    adults = models.PositiveIntegerField(default=1, verbose_name="Взрослые(от 18 лет)")
    teens = models.PositiveIntegerField(default=0, verbose_name="Подростки(от 13-18 лет)")
    children = models.PositiveIntegerField(default=0, verbose_name="Дети(от 2-12 лет)")
    infants = models.PositiveIntegerField(default=0, verbose_name="Младенцы(младше 2)")
    pets = models.PositiveIntegerField(default=0, verbose_name="Домашние животные")
    housing = models.OneToOneField(Housing, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Жилье")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")


class HouseFavorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Housing, on_delete=models.CASCADE)






class Hotel(Housing):
    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"


class Hostel(Housing):
    class Meta:
        verbose_name = "Хостел"
        verbose_name_plural = "Хостелы"


class Apartment(Housing):
    class Meta:
        verbose_name = "Апартаменты"
        verbose_name_plural = "Апартаменты"


class GuestHouse(Housing):
    class Meta:
        verbose_name = "Гостиница"
        verbose_name_plural = "Гостиницы"


class Sanatorium(Housing):
    class Meta:
        verbose_name = "Санаторий"
        verbose_name_plural = "Санатории"
