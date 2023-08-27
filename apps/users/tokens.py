from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
import random

User = get_user_model()


def create_jwt_pair_for_user(user: User):
    refresh = RefreshToken.for_user(user)

    tokens = {"access": str(refresh.access_token), "refresh": str(refresh)}

    return tokens
code = random.randint(1000, 9999)
confirmation_code = random.randint(1000, 9999)
recovery_code = random.randint(1000, 9999)