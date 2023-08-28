from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тест привычек"""

    def setUp(self) -> None:
        """Создание тестовой привычки"""

        self.user = User.objects.create(
            email='test@example.com',
            password='test',
            is_superuser=True,
            is_staff=True,
            chat_telegram_id="ii_ildar",
        )

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place="home",
            time=datetime.now(),
            action="улыбнуться",
            sign_nice_habit=True,
            frequency=1,
            execution_time=10,
            flag_public=True
        )

    def test_1_create_habit(self):
        """ Тестирование создания привычки """

        data = {
            'user': self.user.pk,
            'place': "school",
            'time': datetime.now(),
            'action': "потянуться",
            'sign_nice_habit': True,
            'frequency': 1,
            'execution_time': 10,
            'flag_public': False
        }
        response = self.client.post('/habits/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_2_list_habit(self):
        """ Тестирование вывода списка привычек """

        Habit.objects.create(
            user=self.user,
            place="school",
            time=datetime.now(),
            action="test",
            sign_nice_habit=True,
            frequency=2,
            execution_time=22,
        )

        response = self.client.get('/habits/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_3_list_public_habit(self):
        """ Тестирование вывода списка привычек c флагом публикации """

        response = self.client.get('/habits/public/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_4_retrieve_habit(self):
        """Тестирование вывода одной привычки """

        response = self.client.get(f'/habits/{self.habit.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_4_update_put_habit(self):
        """" Тестирование put обновление привычки"""

        data = {
            'user': self.user.pk,
            'place': 'test',
            'time': '2023-08-11 00:00:00',
            'action': 'test',
            'frequency': 1,
            'execution_time': 20
        }

        response = self.client.patch(f'/habits/update/{self.habit.pk}/',
                                     data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["place"], 'test')

    def test_6_destroy_habit(self):
        """ Тестирование удаления урока """

        response = self.client.delete(f'/habits/delete/{self.habit.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.all().exists())
        self.assertEqual(Habit.objects.all().count(), 0)
