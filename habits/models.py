from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    place = models.CharField(
        max_length=255,
        verbose_name='Место')
    time = models.DateTimeField(
        verbose_name='Время')
    action = models.CharField(
        max_length=255,
        verbose_name='Действие')
    sign_nice_habit = models.BooleanField(
        default=False,
        verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Связанная привычка')
    frequency = models.IntegerField(
        default=1,
        verbose_name='Периодичность в днях')
    award = models.CharField(
        max_length=255,
        **NULLABLE,
        verbose_name='Вознаграждение')
    execution_time = models.IntegerField(
        **NULLABLE,
        verbose_name='Время выполнения')
    flag_public = models.BooleanField(
        default=False,
        verbose_name='Признак публичности')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'
