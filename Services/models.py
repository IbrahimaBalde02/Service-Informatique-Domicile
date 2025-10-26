from django.db import models

class Service(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre du service")
    description = models.TextField(verbose_name="Description du service")
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Prix (en GNF)")
    details = models.TextField(blank=True, null=True, verbose_name="Détails ou sous-services")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["-date_creation"]

    def __str__(self):
        return self.titre
