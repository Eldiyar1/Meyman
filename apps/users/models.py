from django.core.validators import MinValueValidator
from django.db import models
from .constants import *
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, user_type, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, user_type=user_type)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, user_type, password=None):
        user = self.create_user(email, username, user_type, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



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
        upload_to='media/avatars/', blank=True, null=True, verbose_name='Profiles_avatar'
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
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                                     verbose_name="дата бронирование")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())])

    def __str__(self):
        return str(self.user)


class AccommodationReservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    check_in_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Заезд")
    check_out_date = models.DateField(validators=[MinValueValidator(timezone.now().date())], verbose_name="Выезд")

    def __str__(self):
        return str(self.user)




