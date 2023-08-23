from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .manager import CustomUserManager
from .constants import *
from apps.travel.service import compress_image


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'user_type']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to='media/avatars/', blank=True, null=True, verbose_name='Profiles_avatar',
    )
    email = models.EmailField(
        null=True, verbose_name='Email'
    )
    phone_number = PhoneNumberField(
        null=True, verbose_name='Номер телефона',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        compress_image(self)

    def compress_image(self):
        return compress_image(self)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.email


class ReviewSite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        compress_image(self)

    def compress_image(self):
        return compress_image(self)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return str(self.user)
