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

def Accueil(request):
    return render(request,"templates/Accueil.html")

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request,'computerApp/machine_add.html',context)

def personne_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid():
            new_personne = Personnel(nom=form.cleaned_data['nom'])
            new_personne.save()
            return redirect('personnes')
    else:
        form = AddPersonnelForm()
        context = {'form': form}
        return render(request,'computerApp/personne_add.html',context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context={'machine': machine}
    return render(request, 'computerApp/machine_detail.html',context)

def personne_detail_view(request, pk):
    personne = get_object_or_404(Personnel, id=pk)
    context={'personne': personne}
    return render(request, 'computerApp/personne_detail.html',context)
