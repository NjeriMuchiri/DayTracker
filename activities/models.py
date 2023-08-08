from django.db import models
# Create your models here.
class DaysActivities(models.Model):
    date = models.DateField()
    list_of_things = models.CharField(max_length=200)
    productivity_range = models.PositiveIntegerField()

    def __str__(self):
        return self.list_of_things

