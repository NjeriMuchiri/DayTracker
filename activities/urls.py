from django.urls import path
from . import views

app_name = "activities"
urlpatterns = [
    path('home/', views.homeIndex, name="index"),
    path('graph/', views.graph_representation, name="graph_representation")
]
