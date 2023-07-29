from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from apps.travel.models import Housing
from apps.travel_service.models import Transfer
from django.contrib.auth.models import AbstractUser, Group, Permission
from .constants import *
class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set')
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')


    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)

    objects = CustomUser()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
class CarReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Transfer, on_delete=models.CASCADE)
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                     verbose_name="дата бронирование")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())])

    def __str__(self):
        return str(self.user)


class AccommodationReservation(models.Model):


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
