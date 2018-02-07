from django.db import models
from django.utils import timezone

class DailyWorkout(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    text = models.textField()
    title = models.CharField(max_length=200)

    def __init__(self):
        self.text = ""
        self.title = ""

    def __str__(self):
        return self.title


class MonthWorkout(models.Model):
    daysOfThisMonth = [DailyWorkout() for i in range(31)]


class Workout(models.Model):
