from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"templates/index.html")

def Utilisateurs(request):
    return render(request,"templates/Utilisateurs.html")

def Machines(request):
    return render(request,"templates/Machines.html")
