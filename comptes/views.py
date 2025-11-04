from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import FormulaireInscription
from django.contrib.auth.forms import AuthenticationForm

def inscription(request):
    if request.method == 'POST':
        form = FormulaireInscription(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie ! 👋")
            return redirect('services:accueil')
        else:
            messages.error(request, "Erreur dans le formulaire, vérifiez vos informations.")
    else:
        form = FormulaireInscription()
    return render(request, 'comptes/inscription.html', {'form': form})


def connexion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenue {user.username} ! 👋")
            return redirect('services:accueil')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, 'comptes/connexion.html', {'form': form})


def deconnexion(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecté.")
    return redirect('services:accueil')
