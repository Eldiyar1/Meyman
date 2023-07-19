from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class PriceRange(models.Model):
    class Meta:
        verbose_name = "Ценовой диапазон"
        verbose_name_plural = "Ценовые диапазоны"

    min_price = models.PositiveIntegerField(default=10, verbose_name="Минимум")
    max_price = models.PositiveIntegerField(default=500, verbose_name="Максимум")

    def __str__(self):
        return f"Минимум: {self.min_price}$  Максимум: {self.max_price}$"

    def validate_price(self):
        if self.min_price < 10:
            raise ValidationError("Минимальная цена не может быть меньше 10 долларов.")
        if self.max_price > 500:
            raise ValidationError("Максимальная цена не может быть больше 500 долларов.")
        if self.min_price > self.max_price:
            raise ValidationError("Минимальная цена не может быть больше максимальной цены.")


class HousingType(models.Model):
    class Meta:
        verbose_name = "Тип жилья"
        verbose_name_plural = "Типы жилья"

    TYPE_CHOICES = (
        ('Отели', 'Отели'),
        ('Хостелы', 'Хостелы'),
        ('Апартаменты', 'Апартаменты'),
        ('Гостиницы', 'Гостиницы'),
    )

    housing_type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="Тип жилья")

    def __str__(self):
        return self.housing_type


class AccommodationType(models.Model):
    class Meta:
        verbose_name = "Тип размещения"
        verbose_name_plural = "Типы размещения"

    TYPE_CHOICES = (
        ("Жилье целиком", "Жилье целиком"),
        ("Комната", "Комната"),
        ("Общая комната", "Общая комната"),
    )

    accommodation_type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name="Тип размещения")

    def __str__(self):
        return self.accommodation_type


class BedType(models.Model):
    class Meta:
        verbose_name = "Тип кроватей"
        verbose_name_plural = "Типы кроватей"

    TYPE_CHOICES = (
        ("Односпальная", "Односпальная"),
        ("Двуспальная", "Двуспальная"),
    )

    bed_type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name="Тип кроватей")

    def __str__(self):
        return self.bed_type


class Housing(models.Model):
    class Meta:
        abstract = True

    housing_name = models.CharField(max_length=255, verbose_name="Название места жительства")
    image = models.ImageField(upload_to='images/housing/', verbose_name="Изображение места жительства")
    description = models.TextField(verbose_name="Описание места жительства")
    daily_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)],
                                      verbose_name="Цена за сутки")
    available_rooms = models.PositiveIntegerField(verbose_name="Количество доступных комнат")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    is_available = models.BooleanField(default=True, verbose_name="Доступность")
    price_range = models.ForeignKey(PriceRange, on_delete=models.SET_NULL, null=True, verbose_name="Ценовой диапазон")
    housing_type = models.ForeignKey(HousingType, on_delete=models.SET_NULL, null=True, verbose_name="Тип жилья")
    accommodation_type = models.ForeignKey(AccommodationType, on_delete=models.SET_NULL, null=True,
                                           verbose_name="Тип размещения")
    bed_type = models.ForeignKey(BedType, on_delete=models.SET_NULL, null=True, verbose_name="Тип кроватей")

    def __str__(self):
        return self.housing_name


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


class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    fullname = models.CharField(
        max_length=100,
        verbose_name="ФИО автора"
    )

    def __str__(self):
        return self.fullname


class News(models.Model):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/news', verbose_name='Картинка новости', blank=True, null=True)
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="news", verbose_name='Автор')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на источник")

    def __str__(self):
        return self.title

    def author_fullname_list(self):
        return [self.author.fullname]

    def formatted_published_date(self):
        return self.published_date.strftime('%d-%m-%Y')
