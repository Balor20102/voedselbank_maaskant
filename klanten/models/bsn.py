from django.db import models

class BSN(models.Model):
    klant = models.ForeignKey("Klant", on_delete=models.DO_NOTHING, null=True)
    BSN = models.IntegerField()
    volledigenaam = models.CharField(max_length=100)

    def __str__(self):
        return self.volledigenaam