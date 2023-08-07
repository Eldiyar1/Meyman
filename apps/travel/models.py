from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from django.utils import timezone
from apps.travel.constants import HOUSING_CHOICES, ACCOMMODATION_CHOICES, BEDROOM_CHOICES, BED_CHOICES, \
    FOOD_CHOICES, PARKING_CHOICES, HOUSING_AMENITIES_CHOICES, ROOM_AMENITIES_CHOICES, STAR_CHOICES, PAYMENT_CHOICES, \
    RATING_CHOICES, PARKING_LOCATION_CHOICES, ACCOMMODATION_TYPE_CHOICES, BREAKFAST_CHOICES, CANCELLATION_CHOICES, \
    TIME_CHOICES, CHOICES_DA_NET
from apps.travel_service.constants import DESTINATION_CHOICES
from django.utils.text import slugify
from apps.users.email import CustomUser


class Housing(models.Model):
    class Meta:
        verbose_name = "Жильё"
        verbose_name_plural = "Жильё"

    housing_name = models.CharField(max_length=255, verbose_name="Название места жительства")
    description = models.TextField(verbose_name="Описание места жительства")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    region = models.CharField(max_length=50, choices=DESTINATION_CHOICES, verbose_name="Область")
    stars = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                choices=STAR_CHOICES, verbose_name='Количество звезд')
    housing_type = models.CharField(max_length=50, choices=HOUSING_CHOICES, verbose_name="Тип жилья")
    accommodation_type = models.CharField(max_length=50, choices=ACCOMMODATION_CHOICES, verbose_name="Тип размещения")
    food_type = models.CharField(max_length=50, choices=FOOD_CHOICES, default="Не включено", verbose_name="Тип питания")
    housing_amenities = MultiSelectField(choices=HOUSING_AMENITIES_CHOICES, max_length=100,
                                         verbose_name='Удобства в объекте')
    check_in_time_start = models.IntegerField(choices=TIME_CHOICES, verbose_name="Заезд С")
    check_in_time_end = models.IntegerField(choices=TIME_CHOICES, verbose_name="Заезд До")
    check_out_time_start = models.IntegerField(choices=TIME_CHOICES, verbose_name="Отъезд С")
    check_out_time_end = models.IntegerField(choices=TIME_CHOICES, verbose_name="Отъезд До")
    children_allowed = models.BooleanField(default=False, verbose_name='Можно ли проживать с детьми?')
    pets_allowed = models.BooleanField(default=False, verbose_name='Можно ли проживать с домашними животными?')
    pet_fee = models.BooleanField(default=False, verbose_name='Берете ли вы плату за домашних животных?')
    breakfast_offered = models.BooleanField(default=False, verbose_name='Вы предлагаете гостям завтрак?')
    breakfast_included = models.BooleanField(default=False, verbose_name='Завтрак включен в стоимость проживания?')
    breakfast_cost_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                             verbose_name='Стоимость завтрака в US$ (с человека за ночь)')
    breakfast_type = MultiSelectField(choices=BREAKFAST_CHOICES, max_length=100, blank=True, null=True,
                                      verbose_name='Какой тип завтрака вы предлагаете?')
    parking = models.CharField(max_length=10, choices=PARKING_CHOICES, default='no', verbose_name='Услуги парковки')
    parking_cost_usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                           verbose_name='Стоимость парковки в US$ (за день)')
    parking_location = models.CharField(max_length=50, choices=PARKING_LOCATION_CHOICES,
                                        blank=True, null=True,
                                        verbose_name='Местонахождение парковки')

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

class HousingImage(models.Model):
    class Meta:
        verbose_name = 'Изображение места жительства'
        verbose_name_plural = 'Изображения места жительства'

    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='housing_images')
    image = models.ImageField(upload_to='images/housing/', null=True, verbose_name='Изображение места жительства')


class Room(models.Model):
    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='rooms')
    room_name = models.CharField(max_length=50, choices=ACCOMMODATION_TYPE_CHOICES, verbose_name='название номера')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена за ночь")
    room_amenities = MultiSelectField(choices=ROOM_AMENITIES_CHOICES, max_length=100, verbose_name='Удобства номера')
    num_rooms = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)],
                                    verbose_name="Количество комнат в номере")
    bedrooms = models.CharField(max_length=50, choices=BEDROOM_CHOICES, verbose_name="Количество спален")
    bed_type = models.CharField(max_length=50, choices=BED_CHOICES, verbose_name="Тип кроватей")
    single_bed_count = models.PositiveIntegerField(default=0, verbose_name="Количество односпальных кроватей")
    double_bed_count = models.PositiveIntegerField(default=0, verbose_name="Количество двуспальных кроватей")
    queen_bed_count = models.PositiveIntegerField(default=0, verbose_name="Количество широких (queen-size) кроватей")
    king_bed_count = models.PositiveIntegerField(default=0, verbose_name="Количество широких (king-size) кроватей")
    sofa_bed_count = models.PositiveIntegerField(default=0, verbose_name="Количество диван-кроватей")
    max_guest_capacity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(6)],
                                                     verbose_name="Максимальная вместимость гостей в номере")
    room_area = models.PositiveIntegerField(verbose_name="Площадь комнаты(м²)")
    smoking_allowed = models.BooleanField(default=False, verbose_name="Разрешено ли курение в комнате")
    without_card = models.BooleanField(default=True, choices=CHOICES_DA_NET, verbose_name="Без банковской карты")
    free_cancellation = models.BooleanField(default=False, choices=CHOICES_DA_NET, verbose_name="Бесплатная отмена")
    payment = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default="К оплате сейчас", verbose_name="Оплата")
    policy = models.CharField(choices=CANCELLATION_CHOICES, max_length=50, verbose_name='Правила бесплатной отмены')

    def __str__(self):
        return self.room_name


class RoomImage(models.Model):
    class Meta:
        verbose_name = 'Изображение места жительства'
        verbose_name_plural = 'Изображения места жительства'

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    image = models.ImageField(upload_to='images/rooms/', default='', null=True, blank=True, verbose_name='Изображение номера')


class Rating(models.Model):
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='ratings_given')
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='ratings_received')
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, default='0')


class HouseReservation(models.Model):
    class Meta:
        verbose_name = "Бронь жилья"
        verbose_name_plural = "Бронь жилищ"

    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES, verbose_name="Куда")
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Заезд")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Выезд")
    adults = models.PositiveIntegerField(default=1, verbose_name="Взрослые(от 18 лет)")
    teens = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name="Подростки(от 13-18 лет)")
    children = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name="Дети(от 2-12 лет)")
    infants = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name="Младенцы(младше 2)")
    pets = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name="Домашние животные")
    housing = models.OneToOneField(Housing, on_delete=models.CASCADE, verbose_name="Жилье")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")


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
