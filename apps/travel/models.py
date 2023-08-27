from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from django.utils import timezone
from .service import validate_beds, validate_people
from apps.travel.constants import *
from apps.travel_service.constants import DESTINATION_CHOICES
from django.utils.text import slugify
from apps.users.email import CustomUser
from .service import compress_image


class Housing(models.Model):
    housing_name = models.CharField(max_length=255, verbose_name="Название места жительства")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    region = models.CharField(max_length=50, choices=DESTINATION_CHOICES, verbose_name="Область")
    stars = models.IntegerField(default=1, choices=STAR_CHOICES, verbose_name='Количество звезд')
    housing_type = models.CharField(max_length=50, choices=HOUSING_CHOICES, verbose_name="Тип жилья")
    accommodation_type = models.CharField(max_length=50, choices=ACCOMMODATION_CHOICES, verbose_name="Тип размещения")
    food_type = models.CharField(max_length=50, choices=FOOD_CHOICES, default="Не включено", verbose_name="Тип питания")
    free_internet = models.BooleanField(default=False, verbose_name='Бесплатный интернет')
    gym = models.BooleanField(default=False, verbose_name='Спортзал',)
    restaurant = models.BooleanField(default=False, verbose_name='Ресторан')
    airport_transfer = models.BooleanField(default=False, verbose_name='Трансфер от/до аэропорта')
    paid_transfer = models.BooleanField(default=False, verbose_name='Платно за трансфер')
    park = models.BooleanField(default=False, verbose_name='Парковка')
    paid_parking = models.BooleanField(default=False, verbose_name='Платно за парковку')
    spa_services = models.BooleanField(default=False, verbose_name='Спа услуги')
    bar = models.BooleanField(default=False, verbose_name='Бар')
    paid_bar = models.BooleanField(default=False, verbose_name='Платно за бар')
    pool = models.BooleanField(default=False, verbose_name='Бассейн')
    room_service = models.BooleanField(default=False, verbose_name='Обслуживание номеров')
    poolside_bar = models.BooleanField(default=False, verbose_name='Бар у бассейна')
    cafe = models.BooleanField(default=False, verbose_name='Кафе')
    in_room_internet = models.BooleanField(default=False, verbose_name='Доступ в интернет: в номерах')
    hotel_wide_internet = models.BooleanField(default=False, verbose_name='Доступ в интернет: на всей территории отеля')
    check_in_time_start = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name="Заезд С")
    check_in_time_end = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name="Заезд До")
    check_out_time_start = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name="Отъезд С")
    check_out_time_end = models.CharField(max_length=5, choices=TIME_CHOICES, verbose_name="Отъезд До")
    children_allowed = models.BooleanField(default=False, verbose_name='Можно ли проживать с детьми?')
    pets_allowed = models.BooleanField(default=False, verbose_name='Можно ли проживать с домашними животными?')
    pet_fee = models.BooleanField(default=False, verbose_name='Берете ли вы плату за домашних животных?')
    breakfast_offered = models.BooleanField(default=False, verbose_name='Вы предлагаете гостям завтрак?')
    breakfast_included = models.BooleanField(default=False, verbose_name='Завтрак включен в стоимость проживания?')
    breakfast_cost_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                             verbose_name='Стоимость завтрака в US$ (с человека за ночь)')
    breakfast_type = MultiSelectField(choices=BREAKFAST_CHOICES, max_length=100, blank=True, null=True,
                                      verbose_name='Какой тип завтрака вы предлагаете?')
    parking_location = models.CharField(max_length=50, choices=PARKING_LOCATION_CHOICES, blank=True, null=True,
                                        verbose_name='Местонахождение парковки')
    slug = models.SlugField(max_length=255, unique=True, verbose_name="человеко-понятный url", blank=True, null=True)

    def __str__(self):
        return self.housing_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.housing_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Место жительства"
        verbose_name_plural = "Места жительства"


class HousingReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    housing = models.ForeignKey("Housing", on_delete=models.CASCADE, verbose_name='Название места жительства',
                                related_name='reviews')
    comment = models.TextField(max_length=500, blank=True, null=True, verbose_name='Комментарий')
    date_added = models.DateField(auto_now_add=True, verbose_name="Дата")
    cleanliness_rating = models.IntegerField(choices=RATING_CHOICES, verbose_name='Чистота')
    comfort_rating = models.IntegerField(choices=RATING_CHOICES, verbose_name='Комфорт')
    staff_rating = models.IntegerField(choices=RATING_CHOICES, verbose_name='Персонал')
    value_for_money_rating = models.IntegerField(choices=RATING_CHOICES,
                                                 verbose_name='Цена/Качества')
    food_rating = models.IntegerField(choices=RATING_CHOICES, verbose_name='Питание')
    location_rating = models.IntegerField(choices=RATING_CHOICES, verbose_name='Местоположение')

    def __str__(self):
        return f"Отзыв от {self.user} на {self.housing}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class HousingImage(models.Model):
    image = models.ImageField(upload_to='housing', verbose_name="Изображения мест жительств")
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='housing_images')

    def __str__(self):
        return f"Image for {self.housing.housing_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        compress_image(self)

    def compress_image(self):
        return compress_image(self)

    class Meta:
        verbose_name = 'Изображение места жительства'
        verbose_name_plural = 'Изображения места жительств'


class HousingReservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, verbose_name="Название места жительства")
    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES, verbose_name="Куда")
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Заезд")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Выезд")
    adults = models.PositiveIntegerField(default=1, verbose_name="Взрослые(от 18 лет)")
    teens = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name="Подростки(от 13-18 лет)")
    children = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name="Дети(от 2-12 лет)")
    client_email = models.EmailField(null=True, blank=True, verbose_name="Email клиента")
    def __str__(self):
        return f"Бронь жилья для {self.user}"
    def clean(self):
        validate_people(self.adults, self.teens, self.children)


    class Meta:
        verbose_name = "Бронь жилья"
        verbose_name_plural = "Бронь жилищ"


class HistoryReservation(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reservation = models.ForeignKey(HousingReservation, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "История бронирований"


class Room(models.Model):
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, verbose_name="Название места жительства",
                                related_name='rooms')
    room_name = models.CharField(max_length=100, choices=ACCOMMODATION_TYPE_CHOICES, verbose_name='название номера')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена за ночь")
    room_amenities = MultiSelectField(choices=ROOM_AMENITIES_CHOICES, max_length=255, verbose_name='Удобства')
    kitchen = MultiSelectField(choices=KITCHEN_CHOICES, max_length=255, verbose_name="Кухня")
    amenities = MultiSelectField(choices=OUTSIDE_CHOICES, max_length=255, verbose_name="На улице")
    bathroom = MultiSelectField(choices=BATHROOM_AMENITIES_CHOICES, max_length=255, verbose_name="Ванная")
    num_rooms = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)],
                                    verbose_name="Количество комнат в номере")
    bedrooms = models.CharField(max_length=50, choices=BEDROOM_CHOICES, verbose_name="Количество спален")
    bed_type = MultiSelectField(choices=BED_CHOICES, max_length=100, verbose_name="Тип кроватей")
    single_bed = models.PositiveIntegerField(default=1, verbose_name="Односпальных кроватей")
    double_bed = models.PositiveIntegerField(verbose_name="Двуспальных кроватей", null=True, blank=True)
    queen_bed = models.PositiveIntegerField(verbose_name="Широких (queen-size) кроватей", null=True, blank=True)
    king_bed = models.PositiveIntegerField(verbose_name="Широких (king-size) кроватей", null=True, blank=True)
    sofa_bed = models.PositiveIntegerField(verbose_name="Диван-кроватей", null=True, blank=True)
    max_guest_capacity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(6)],
                                                     verbose_name="Максимальная вместимость гостей в номере")
    room_area = models.PositiveIntegerField(verbose_name="Площадь комнаты(м²)")
    smoking_allowed = models.BooleanField(default=False, verbose_name="Разрешено ли курение в комнате")

    def __str__(self):
        return self.room_name

    def clean(self):
        validate_beds(self.single_bed, self.double_bed, self.queen_bed, self.king_bed, self.sofa_bed)

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class HousingAvailability(models.Model):
    housing = models.ForeignKey(Housing, related_name='availability', on_delete=models.CASCADE,
                                verbose_name='Место жительство')
    date = models.DateField(verbose_name='Дата')
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Календарь'
        verbose_name_plural = 'Календари'
        unique_together = ('housing', 'date')


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    image = models.ImageField(upload_to='rooms', verbose_name="Изображения номера")

    def __str__(self):
        return f"Image for {self.room.room_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        compress_image(self)

    def compress_image(self):
        return compress_image(self)

    class Meta:
        verbose_name = 'Изображение номера'
        verbose_name_plural = 'Изображения номеров'
