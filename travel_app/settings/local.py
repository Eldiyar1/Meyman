from .base import *
from .development import *
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:3080",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:4040",
    "https://ae97-212-112-103-156.ngrok-free.app",
]
LOCAL_HOST = ['*']
ALLOWED_HOSTS = LOCAL_HOST + CORS_ALLOWED_ORIGINS


CSRF_TRUSTED_ORIGINS = ["https://ae97-212-112-103-156.ngrok-free.app"]
