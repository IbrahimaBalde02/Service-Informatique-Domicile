from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from Services.models import Service

@login_required
def redirect_dashboard(request):
    if request.user.role == 'client':
        return redirect('dashboard:client')
    elif request.user.role == 'prestataire':
        return redirect('dashboard:prestataire')
    return HttpResponseForbidden("Rôle non reconnu.")


@login_required
def dashboard_client(request):
    if request.user.role != 'client':
        return HttpResponseForbidden("Accès interdit.")

    services = Service.objects.all()

    context = {
        'services': services
    }
    return render(request, 'dashboard/client.html', context)

@login_required
def dashboard_prestataire(request):
    if request.user.role != 'prestataire':
        return HttpResponseForbidden("Accès interdit.")
    return render(request, 'dashboard/prestataire.html')
