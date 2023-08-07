from django.urls import path
from . import views

app_name = "activities"
urlpatterns = [
    path('', views.homeIndex, name="index"),
    path('donelist/',views.listDone, name="complete"),
    path('graph/', views.graph_representation, name="graph_representation"),
]
