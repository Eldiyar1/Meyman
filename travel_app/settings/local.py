from .base import *
from .development import *

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:3080",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:4040",
    "https://f683-185-138-186-141.ngrok-free.app",
]
ALLOWED_HOSTS = ['*'] + CORS_ALLOWED_ORIGINS


CSRF_TRUSTED_ORIGINS = ["https://f683-185-138-186-141.ngrok-free.app"]
