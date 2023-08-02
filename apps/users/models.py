from django.core.validators import MinValueValidator
from django.db import models
from apps.travel.models import Housing
from apps.travel_service.models import Transfer
from django.contrib.auth.models import AbstractBaseUser,  PermissionsMixin
from .constants import *
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to='avatars/', blank=True, null=True, verbose_name='Profiles_avatar'
    )
    email = models.EmailField(
        null=True, verbose_name='Email'
    )
    phone_number = PhoneNumberField(
        null=True, verbose_name='Номер телефона'
    )

    def __str__(self):
        return self.email
class CarReservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                     verbose_name="дата бронирование")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())])

    def __str__(self):
        return str(self.user)


class AccommodationReservation(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Housing, on_delete=models.CASCADE)
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Заезд")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Выезд")
    booking_type = models.CharField(max_length=50, choices=BOOKING_CHOICES, default="Без банковской карты",
                                    verbose_name="Бронирование")
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default="К оплате сейчас",
                                    verbose_name="Оплата")

    def __str__(self):
        return str(self.user)

class AdminReview(models.Model):
    author = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.author

