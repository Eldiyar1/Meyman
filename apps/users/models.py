from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from apps.travel.models import Housing
from apps.travel_service.models import Transfer
from django.contrib.auth.models import AbstractUser


# class Profile(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE
#     )
#     avatar = models.ImageField(
#         upload_to='avatars/', blank=True, null=True, verbose_name='Profiles_avatar'
#     )
#     email = models.EmailField(
#         null=True, verbose_name='Email'
#     )
#     phone_number = PhoneNumberField(
#         null=True, verbose_name='Номер телефона'
#     )

#     def __str__(self):
#         return self.email

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/', blank=True, null=True, verbose_name='Profiles_avatar'
    )
    phone_number = PhoneNumberField(
        null=True, verbose_name="Номер телефона"
    )


class CarReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                     verbose_name="дата бронирование")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())])

    def __str__(self):
        return str(self.user)


class AccommodationReservation(models.Model):
    BOOKING_CHOICES = (
        ("Без банковской карты", "Без банковской карты"),
        ("Бесплатная отмена", "Бесплатная отмена"),
    )

    PAYMENT_CHOICES = (
        ("К оплате сейчас", "К оплате сейчас"),
        ("Предоплата", "Предоплата"),
        ("Оплата наличными", "Оплата наличными"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Housing, on_delete=models.CASCADE)
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Заезд")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Выезд")
    booking_type = models.CharField(max_length=50, choices=BOOKING_CHOICES, default="Без банковской карты",
                                    verbose_name="Бронирование")
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default="К оплате сейчас",
                                    verbose_name="Оплата")

    def __str__(self):
        return str(self.user)
