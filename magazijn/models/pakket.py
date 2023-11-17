from django.db import models
        
class Pakket(models.Model):
        gezinsnaam = models.ForeignKey("klanten.Klant", on_delete=models.DO_NOTHING, null=True)
        productitem = models.ForeignKey("ProductItem", on_delete=models.DO_NOTHING, null=True)
        uitgiftdatum = models.DateField()

        def __str__(self):
            return self.GezinsNaam
