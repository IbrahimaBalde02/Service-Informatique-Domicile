from django.shortcuts import render
from .models import Service

# Vue d'accueil
def accueil(request):
    """Page d'accueil du site DomServices."""
    return render(request, 'Services/index.html')


# Vue listant tous les services
def liste_services(request):
    """Affiche la liste de tous les services disponibles."""
    services = Service.objects.all().order_by('-date_creation')  # tri du plus récent au plus ancien
    return render(request, 'Services/liste_services.html', {'services': services})


# Vue de contact
def contact(request):
    """Page de contact."""
    return render(request, 'Services/contact.html')


# Vue À propos
def apropos(request):
    """Page à propos du site."""
    return render(request, 'Services/apropos.html')
