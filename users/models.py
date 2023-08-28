from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Класс для отображения пользователей"""

    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    chat_telegram_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=' Ссылка на телеграмм')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
