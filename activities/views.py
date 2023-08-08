from django.shortcuts import render, redirect
from .models import DaysActivities
import matplotlib.pyplot as plt
from .forms import DayAboutForm
from io import BytesIO
import base64

# Create your views here.
def homeIndex(request):
    form = DayAboutForm()
    if request.method == 'POST':
        form = DayAboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("activities:index")
    context = {'form': form}
    return render(request, 'activities/index.html', context)

def listDone(request):
    doneList = DaysActivities.objects.all()
    context = {'doneList': doneList}
    return render(request,'activities/done_list.html', context)

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

def updateThing(request, pk):
    updates = DaysActivities.objects.get(id=pk)
    form = DayAboutForm(request.POST)
    if form.is_vald():
        form.save()
        return redirect('activities: update')
    context = {'updates': updates}
    return render(request, 'activities/index.html', context)

def deleteThing(request, pk):
    rids = DaysActivities.objects.get(id=pk)
    if request.method == 'POST':
        rids.delete()
        return redirect("activities:deleting")
    return render(request, 'activities/done_list.html', {'rids': rids})
