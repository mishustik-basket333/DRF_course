from datetime import date

from celery import shared_task
from telebot import TeleBot

from habits.models import Habit

api_telegram = '6528415058:AAFsjNe4U70cbbdg83NBX6FVwgQFYNJTCeI'

@shared_task
def get_list_habits():
    """ Получение списка привычек"""

    list_habits = Habit.objects.all()

    for habit in list_habits:

        if habit.time == date.now():
            send_telegram(habit.id)


def send_telegram(id_habit):
    """ Отправка сообщения"""

    habit = Habit.objects.get(pk=id_habit)

    bot = TeleBot(api_telegram)

    message = f'Привет, тебе нужно сделать {habit.action} в {habit.action}'

    bot.send_message(habit.user.chat_telegram_id, message)
