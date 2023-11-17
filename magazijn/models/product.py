from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    EAN = models.IntegerField()
    afbeelding = models.ImageField(upload_to='images/', null=True)
    varkesvlees = models.BooleanField()
    vegataries = models.BooleanField()
    veganistisch = models.BooleanField()
    catagorieën = models.ManyToManyField("Catagorie", related_name="product")
    voorraad = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    