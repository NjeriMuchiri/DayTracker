from django.shortcuts import render, redirect
from .models import DaysActivities
from .forms import DayAboutForm
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Create your views here.
def homeIndex(request):
    form = DayAboutForm()
    if request.method == 'POST':
        form = DayAboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('graph_representation')
    context = {'form': form}
    return render(request, 'activities/index.html', context)

def graph_representation(request):
    recordings = DaysActivities.objects.all()
    dates = [recording.date for recording in recordings]
    productivity_range = [recording.productivity_range for recording in recordings]

    #Creating a line graph using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(dates, productivity_range, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Productivity Level')
    plt.title('Daily Productivity')
    plt.xticks(rotation=45)
    plt.tight_layout()

    #save the plot to a BytesIO object to render in the template
    buffer = BytesIO
    plt.savefig(buffer, format='png')
    plt.close()

    #convert the buffer to base64 encoded string
    graph_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    context = {'graph_image': graph_image}
    return render(request, 'graph_representation.html', context)
