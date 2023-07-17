from django.db import models
from django.contrib.auth.models import User


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
        ordering = ['start_date']

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

    def formatted_start_date(self):
        return self.start_date.strftime('%d-%m-%Y')

    def formatted_end_date(self):
        return self.end_date.strftime('%d-%m-%Y')


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


class Signal(models.Model):
    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомление"

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Кому'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name='Прочитанно'

    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Когда написанно'
    )
    def __str__(self):
        return self.message


def create_signal(user, message):
    notification = Signal(recipient=user, message=message)
    notification.save()
