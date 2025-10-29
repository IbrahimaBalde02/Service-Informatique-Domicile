from django.shortcuts import render
from django.core.mail import send_mail
from .models import Service
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Vue d'accueil
def accueil(request):
    """Page d'accueil du site DomServices."""
    return render(request, 'Services/index.html')


# Vue listant tous les services
def liste_services(request):
    """Affiche la liste de tous les services disponibles."""
    services = Service.objects.all().order_by('-date_creation')  # tri du plus récent au plus ancien
    return render(request, 'Services/liste_services.html', {'services': services})


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages  # <- pour les messages flash
from .forms import ContactForm

def contact_view(request):
    success = False  # on garde ta variable

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            contenu_message = f"Nom : {name}\nEmail : {email}\n\nMessage :\n{message}"

            send_mail(
                subject=subject,
                message=contenu_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            success = True
            form = ContactForm()  # Réinitialiser le formulaire après envoi

            # Ajouter le message flash pour l'accueil
            messages.success(request, "Votre message a bien été envoyé ! Merci ! Nous vous répondrons dès que possible.")

            # Redirection vers la page d'accueil
            return redirect('services:accueil')

    else:
        form = ContactForm()

    return render(request, 'Services/contact.html', {'form': form, 'success': success})


# Vue À propos
def apropos(request):
    """Page à propos du site."""
    return render(request, 'Services/apropos.html')
