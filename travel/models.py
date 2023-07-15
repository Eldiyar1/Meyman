from django.db import models


class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    fullname = models.CharField(
        max_length=150,
        verbose_name="ФИО автора"
    )

    def __str__(self):
        return self.fullname


class Hotel(models.Model):
    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"

    hotel_name = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    daily_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за сутки"
    )
    available_rooms = models.PositiveIntegerField(
        verbose_name="Доступные комнаты"
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="Доступность"
    )

    def __str__(self):
        return self.hotel_name


class TravelService(models.Model):
    class Meta:
        verbose_name = "Тревел сервис"
        verbose_name_plural = "Тревел сервисы"

    service_name = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )
    location = models.CharField(
        max_length=255,
        verbose_name="Местоположение"
    )
    start_date = models.DateField(
        verbose_name="Дата начала"
    )
    end_date = models.DateField(
        verbose_name="Дата окончания"
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступность'
    )

    def __str__(self):
        return self.service_name


class News(models.Model):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    content = models.TextField(
        verbose_name="Содержание"
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="news",
        verbose_name='Автор'
    )
    published_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.title

    def author_fullname_list(self):
        return [self.author.fullname]

    def formatted_published_date(self):
        return self.published_date.strftime('%d-%m-%Y')