from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="exercise-home"),
    path('about/', views.about, name="exercise-about"),
]
