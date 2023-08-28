from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from apps.users import models
from .emails import send_email_confirmation
from .models import CustomUser
# from .tokens import confirmation_code, recovery_code

class RegisterService:
    @staticmethod
    def create_user(serializer, request):
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_email_confirmation(user.email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifyService:
    @staticmethod
    def verify_code(serializer):
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        code = serializer.data['verify_code']

        user = CustomUser.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'Неверный email.'}, status=400)

        if user.verify_code != code:
            return Response({'error': 'Неверный код подтверждения.'}, status=400)

        user.is_active = True
        user.save()

        return Response({'message': 'Аккаунт успешно подтвержден.'}, status=200)

