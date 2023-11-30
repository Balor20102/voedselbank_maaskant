from django.db import models

# Create your models here.
class Leverancier(models.Model):
    bedrijfsnaam = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    contactpersoon = models.CharField(max_length=100)
    telefoon = models.IntegerField()
    email = models.EmailField()
    leveringsdatum = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.bedrijfsnaam



