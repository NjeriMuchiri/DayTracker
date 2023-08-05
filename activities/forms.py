from django.forms import ModelForm
from .models import DaysActivities

class DayAboutForm(ModelForm):
    class Meta:
        model = DaysActivities
        fields = '__all__'
