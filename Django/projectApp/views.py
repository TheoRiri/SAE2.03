from django.shortcuts import render, redirect,get_object_or_404
from .models import Machine,Personnel
from .forms import AddMachineForm, AddPersonnelForm
def index(request):
    return render(request,"templates/index.html")

def Utilisateurs(request):
    personnels=Personnel.objects.all()
    context ={
        'personnels' : personnels,
    }
    return render(request,"templates/Utilisateurs.html",context)

def Machines(request):
    machines=Machine.objects.all()
    context ={
        'machines' : machines,
    }
    return render(request,"templates/Machines.html",context)
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('Machines')
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request,'templates/machine_add.html',context)


def Accueil(request):
    return render(request,"templates/Accueil.html")

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('Machines')
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request,'templates/machine_add.html',context)

def personne_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid():
            new_personne = Personnel(nom=form.cleaned_data['nom'])
            new_personne.save()
            return redirect('Utilisateurs')
    else:
        form = AddPersonnelForm()
        form.fields['mach'].choices = Machine.TYPE
        context = {'form': form}
        return render(request,'templates/personne_add.html',context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context={'machine': machine}
    return render(request, 'templates/machine_detail.html',context)

def personne_detail_view(request, pk):
    personne = get_object_or_404(Personnel, id=pk)
    context={'personne': personne}
    return render(request, 'templates/personne_detail.html',context)

def supprimer_utilisateurs(request):
    if request.method == 'POST':
        utilisateurs_a_supprimer = request.POST.getlist('utilisateurs_a_supprimer') 
        return redirect('Utilisateurs')
    return render(request, 'Utilisateurs.html')