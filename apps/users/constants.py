from django.contrib.auth.base_user import BaseUserManager

BOOKING_CHOICES = (
        ("Без банковской карты", "Без банковской карты"),
        ("Бесплатная отмена", "Бесплатная отмена"),
    )
PAYMENT_CHOICES = (
        ("К оплате сейчас", "К оплате сейчас"),
        ("Предоплата", "Предоплата"),
        ("Оплата наличными", "Оплата наличными"),
    )
USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('owner', 'Owner'),
    )



class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)