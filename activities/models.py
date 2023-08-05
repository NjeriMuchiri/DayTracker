from django.db import models
# Create your models here.
class DaysActivitie(models.Model):
    date = models.DateField()
    list_of_things = models.CharField(max_length=200)
    productivity_range = models.PositiveIntegerField()
    
