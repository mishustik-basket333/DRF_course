from rest_framework import serializers

from habits.models import Habit
from habits.validators import double_reward_validator, frequency_validator, sing_nice_habit_validator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            double_reward_validator,
            frequency_validator,
            sing_nice_habit_validator
        ]



