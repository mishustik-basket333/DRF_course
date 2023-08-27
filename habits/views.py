from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.pagination import HabitsPagination
from habits.serializers import HabitSerializer
# from habits.permissions import OwnerPermission


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        data_habit = serializer.save()
        data_habit.user = self.request.user
        data_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """ Вывод списка привычек для пользователя """

    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """ Вывод списка привычек с публикацией == True """

    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(flag_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одной привычки"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Обновление привычки"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
