from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Utilisateurs/', views.Utilisateurs, name='Utilisateurs'),
    path('Machines/', views.Machines, name='Machines'),
    path('Accueil/', views.Accueil, name='Accueil'),
    path('add-machine/',views.machine_add_form,name='add-machine'),
    path('add-personne/',views.personne_add_form,name='add-personne'),
    path('personnes/<pk>', views.personne_detail_view, name='personne-detail'),
    path('machines/<pk>', views.machine_detail_view, name='machine-detail'),
    path('supprimer-machines/', views.supprimer_machines, name='supprimer-machines'),
    path('supprimer-utilisateurs/', views.supprimer_utilisateurs, name='supprimer-utilisateurs'),
    path('modifier-etat-machine/', views.modifier_etat_machine, name='modifier-etat-machine'),
]
