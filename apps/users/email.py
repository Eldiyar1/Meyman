from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.core.mail import send_mail

from .tokens import code
CustomUser = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None






def send_email_confirmation(email):
    from .models import CustomUser

    subject = 'Подтверждение регистрации'
    message = f'Здравствуйте! Ваш адрес электронной почты был указан для входа на приложение Meyman Пожалуйста, введите этот код на странице авторизации:/' \
              f'{code}/' \
              f' Если это не вы или вы не регистрировались на сайте, то просто проигнорируйте это письмо'
    email_from = 'abdykadyrovsyimyk0708@gmail.com'
    send_mail(subject, message, email_from, [email])
    user_obj = CustomUser.objects.get(email=email)
    user_obj.verify_code = code
    user_obj.save()

def send_email_reset_password(email):

    subject = "Восстановление пароля"
    message = f"Код для восстановления пароля: {code} Код действителен в течении 5 минут"
    email_from = 'abdykadyrovsyimyk0708@gmail.com'
    send_mail(subject, message, email_from, [email])