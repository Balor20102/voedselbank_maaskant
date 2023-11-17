from django.db import models

# Create your models here.

class Klant(models.Model):
    gezinsnaam = models.CharField(max_length=100)
    volwassenen = models.IntegerField()
    kinderen = models.IntegerField()
    babies = models.IntegerField()
    postcode = models.CharField(max_length=50)
    varkesvlees = models.BooleanField()
    vegataries = models.BooleanField()
    veganistisch = models.BooleanField()
    alergieën = models.ManyToManyField("Alergie", related_name="klant")

    def __str__(self):
        return self.gezinsnaam