from django.urls import path
from . import views

app_name = "activities"
urlpatterns = [
    path('', views.homeIndex, name="index"),
    path('donelist/',views.listDone, name="complete"),
    path('update_thing/<int:thing_id>/',views.updateThing, name="update"),
    path('delete_thing/<int:thing_id>/',views.deleteThing, name="deleting"),
    path('graph/', views.graph_representation, name="graph_representation"),
]
