from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from apps.travel.models import Housing
from apps.travel_service.models import Transfer


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
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

    def __str__(self):
        return str(self.user)

class AdminReview(models.Model):
    author = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
