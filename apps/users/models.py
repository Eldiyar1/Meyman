from django.core.validators import MinValueValidator
from django.db import models
from .constants import *
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .service import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']
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
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    def __str__(self):
        return self.email


class ReviewSite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return str(self.user)
