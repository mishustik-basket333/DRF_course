from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """ Создание тестового пользователя"""

    def setUp(self) -> None:
        """ Создание тестовых данных"""
        pass
        self.data = {
            "email": "test@lalala.ru",
            "password": "123456",
            "chat_telegram_id": "123456",
        }

    def test_1_create_user(self):
        """ Тестирование создания юзера """

        response = self.client.post('/users/create/', data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 1)
