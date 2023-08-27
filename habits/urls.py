from django.urls import path

from habits.views import HabitCreateAPIView, HabitListAPIView, HabitPublicListAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = 'habits'

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habits_create'),
    path('', HabitListAPIView.as_view(), name='habits'),
    path('public/', HabitPublicListAPIView.as_view(), name='habits_public'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
