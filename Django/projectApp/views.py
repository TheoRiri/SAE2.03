from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"templates/index.html")

def Utilisateurs(request):
    return render(request,"templates/Utilisateurs.html")

def Machines(request):
    return render(request,"templates/Machines.html")

def Accueil(request):
    return render(request,"templates/Accueil.html")

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')

def personne_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid():
            new_personne = Machine(nom=form.cleaned_data['nom'])
            new_personne.save()
            return redirect('personnes')
