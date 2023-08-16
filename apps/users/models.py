from django.core.validators import MinValueValidator
from django.db import models
from .constants import *
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .service import CustomUserManager
from PIL import Image


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
        upload_to='media/avatars/', blank=True, null=True, verbose_name='Profiles_avatar',
    )
    email = models.EmailField(
        null=True, verbose_name='Email'
    )
    phone_number = PhoneNumberField(
        null=True, verbose_name='Номер телефона',
    )

    def __str__(self):
        return self.email

    def compress_image(self):
        img = Image.open(self.avatar.path)
        img = img.convert('RGB')
        img.thumbnail((800, 800))
        img.save(self.avatar.path, 'JPEG', quality=90)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.compress_image()


