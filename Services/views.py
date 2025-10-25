from django.shortcuts import render
from .models import Service

def accueil(request):
    return render(request, 'Services/index.html')

def liste_services(request):
    services = Service.objects.all()  # Récupère tous les services
    return render(request, 'Services/liste_services.html', {'services': services})

def contact(request):
    return render(request, 'Services/contact.html')

def apropos(request):
    return render(request, 'Services/apropos.html')

