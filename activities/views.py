from django.shortcuts import render, redirect
from .models import DaysActivities
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Create your views here.
def homeIndex(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        list_of_things = request.POST.get('list_of_things')
        productivity_range = request.POST.get('productivity_range')
        DaysActivities.objects.create(date=date,list_of_things=list_of_things,productivity_range=productivity_range)
    return render(request, 'activities/index.html')

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
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    #convert the buffer to base64 encoded string
    graph_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    context = {'graph_image': graph_image}
    return render(request, 'activities/graph_representation.html', context)
