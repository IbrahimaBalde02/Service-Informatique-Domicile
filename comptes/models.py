from django.db import models
from django.contrib.auth.models import AbstractUser


class Utilisateur(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('prestataire', 'Prestataire'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
