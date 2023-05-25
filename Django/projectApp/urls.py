from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Utilisateurs/', views.Utilisateurs, name='Utilisateurs'),
    path('Machines/', views.Machines, name='Machines'),
    path('Accueil/', views.Accueil, name='Accueil'),
    path('add-machine',views.machine_add_form,name='add-machine'),
    path('add-personne',views.personne_add_form,name='add-personne'),
]
