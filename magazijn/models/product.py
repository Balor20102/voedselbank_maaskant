from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    EAN = models.IntegerField()
    afbeelding = models.ImageField(upload_to='images/', null=True)
    varkesvlees = models.BooleanField(default=False)
    vegataries = models.BooleanField(default=False)
    veganistisch = models.BooleanField(default=False)
    catagorieën = models.ManyToManyField("Catagorie", related_name="product")
    voorraad = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    