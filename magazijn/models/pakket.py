from django.db import models
from django.utils import timezone
class Pakket(models.Model):
        
        STATUS_CHOICES = (
            (1, 'opgehaald'),
            (2, 'niet opgehaald'),
        )
        gezinsnaam = models.ForeignKey("klanten.Klant", on_delete=models.SET_NULL, null=True)
        uitgiftdatum = models.DateField(default=timezone.now() + timezone.timedelta(weeks=1))
        status = models.IntegerField(default=1, choices=STATUS_CHOICES)
        aangemaakt_op = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            if self.gezinsnaam:
                return f"{self.gezinsnaam.gezinsnaam} - Uitgiftdatum: {self.uitgiftdatum}"
            else:
                return f"Geen gezinsnaam - Uitgiftdatum: {self.uitgiftdatum}"
