from rest_framework.serializers import ValidationError


def double_reward_validator(data):
    if data.get('related_habit') and data.get('award'):
        raise ValidationError('Вы не можете указать одновременно "вознаграждение" '
                              'и "связанную привычку". Выберите что-то одно')


def frequency_validator(data):
    if data.get('frequency') > 7:
        raise ValidationError('Вы не можете выполнять привычку реже, чем раз в 7 дней')


def sing_nice_habit_validator(data):
    if data.get('sign_nice_habit'):
        if data.get('award') or data.get('related_habit'):
            raise ValidationError('Вы не можете вместе с "приятной привычкой"'
                                  ' иметь "вознаграждение" или "связанную привычку"')


def execution_time_validator(data):
    if data.get('execution_time') > 120:
        raise ValidationError('Вы не можете выполнять привычку больше 120 секунд')


def related_habit_validator(data):
    if data.get('related_habit') and not data.get('sign_nice_habit'):
        raise ValidationError('В "связанные привычки" могут попадать только привычки с "признаком приятной привычки"')
