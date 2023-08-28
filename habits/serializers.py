from rest_framework import serializers

from habits.models import Habit
from habits.validators import double_reward_validator, \
    frequency_validator, sing_nice_habit_validator, \
    related_habit_validator, execution_time_validator


class HabitSerializer(serializers.ModelSerializer):
    """ Класс сериализатор привычки """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            double_reward_validator,
            frequency_validator,
            sing_nice_habit_validator,
            execution_time_validator,
            related_habit_validator,
        ]
