from django.shortcuts import render, redirect, get_object_or_404
from .models import Machine, Personnel
from .forms import AddMachineForm, AddPersonnelForm, DeleteMachineForm
from .models import Machine

def index(request):
    return render(request, "index.html")

def Utilisateurs(request):
    personnels = Personnel.objects.all()
    context = {
        'personnels': personnels,
    }
    return render(request, "templates/Utilisateurs.html", context)

def Accueil(request):
    return render(request, "templates/Accueil.html")
    return render(request, "Utilisateurs.html", context)

def Machines(request):
    machines = Machine.objects.all()
    context = {
        'machines': machines,
    }
    return render(request, "Machines.html", context)

def machine_add_form(request):
    machines = Machine.objects.all()
    if request.method == 'POST':
        form = AddMachineForm(request.POST)
        delete_form = DeleteMachineForm(request.POST)

        if form.is_valid():
            nom = form.cleaned_data['nom']
            mach = form.cleaned_data['mach']
            utilisateur = form.cleaned_data['utilisateur']  # Récupérer l'utilisateur sélectionné

            new_machine = Machine(nom=nom, mach=mach, utilisateur=utilisateur)  # Enregistrer l'utilisateur dans la machine
            new_machine.save()
            return redirect('Machines')

        elif delete_form.is_valid():
            machine_id = delete_form.cleaned_data['machine']
            machine = get_object_or_404(Machine, id=machine_id)
            machine.delete()
            return redirect('Machines')

    else:
        form = AddMachineForm()
        delete_form = DeleteMachineForm()
    
    context = {
        'form': form,
        'delete_form': delete_form,
        'machines': machines,
    }
    return render(request, 'machine_add.html', context)

def personne_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST)
        if form.is_valid():
            new_personne = Personnel(nom=form.cleaned_data['nom'])
            new_personne.save()
            return redirect('Utilisateurs')
    else:
        form = AddPersonnelForm()
    
    context = {'form': form}
    return render(request, 'personne_add.html', context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine': machine}
    return render(request, 'machine_detail.html', context)

def personne_detail_view(request, pk):
    personne = get_object_or_404(Personnel, id=pk)
    context = {'personne': personne}
    return render(request, 'personne_detail.html', context)

def supprimer_machines(request):
    if request.method == 'POST':
        utilisateurs_a_supprimer = request.POST.getlist('utilisateurs_a_supprimer')
        machines_to_delete = Machine.objects.filter(id__in=utilisateurs_a_supprimer)
        machines_to_delete.delete()
        return redirect('Machines')
    
    return redirect('Machines')

def supprimer_utilisateurs(request):
    if request.method == 'POST':
        utilisateurs_a_supprimer = request.POST.getlist('utilisateurs_a_supprimer')
        utilisateurs_to_delete = Personnel.objects.filter(id__in=utilisateurs_a_supprimer)
        utilisateurs_to_delete.delete()
        return redirect('Utilisateurs')
    
    return redirect('Utilisateurs')

def modifier_etat_machine(request):
    if request.method == 'POST':
        machine_ids = request.POST.getlist('etat_machine')
        for machine_id in machine_ids:
            machine = get_object_or_404(Machine, id=machine_id)
            machine.etat_en_ligne = not machine.etat_en_ligne  # Inverse l'état
            machine.save()
        # Faire d'autres actions si nécessaire

    machines = Machine.objects.all()
    return render(request, 'Machines.html', {'machines': machines})