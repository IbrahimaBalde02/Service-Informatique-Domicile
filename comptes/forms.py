from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class FormulaireInscription(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'telephone', 'adresse', 'role', 'password1', 'password2']
