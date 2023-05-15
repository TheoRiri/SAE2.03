from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Utilisateurs/', views.Utilisateurs, name='Utilisateurs'),
    path('Machines/', views.Machines, name='Machines'),
]
