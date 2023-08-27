from rest_framework.serializers import ValidationError


def double_reward_validator(data):
    if data.get('related_habit') and data.get('award'):
        raise ValidationError('Вы не можете указать одновременно "вознаграждение" '
                              'и "приятную привычку". Выберите что-то одно')


def frequency_validator(data):
    if data.get('frequency') > 7:
        raise ValidationError('Вы не можете выполнять привычку реже, чем раз в 7 дней')


def sing_nice_habit_validator(data):
    if data.get('sign_nice_habit'):
        if data.get('award') or data.get('related_habit'):
            raise ValidationError('Вы не можете вместе с приятной привычкой'
                                  ' иметь вознаграждение или связанную привычку')


def execution_time_validator(data):
    if data.get('execution_time') > 120:
        raise ValidationError('Вы не можете выполнять привычку больше 120 секунд')







# 1Исключить одновременный выбор связанной привычки и указания вознаграждения.
# 5Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
# 4У приятной привычки не может быть вознаграждения или связанной привычки.
# 2Время выполнения должно быть не больше 120 секунд.

# 3В связанные привычки могут попадать только привычки с признаком приятной привычки.

