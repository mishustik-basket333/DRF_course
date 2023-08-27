from django.contrib import admin

from habits.models import Habit


# Register your models here.
@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("user", "place", "time", "action",)
    list_filter = ("user",)
    search_fields = ("user", "action",)
