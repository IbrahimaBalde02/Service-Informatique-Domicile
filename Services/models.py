from django.db import models

class Service(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    details = models.TextField(blank=True, null=True)  # Sous-services comme Word, Excel, etc.
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
