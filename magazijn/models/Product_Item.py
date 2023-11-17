from django.db import models

# Create your models here.
class ProductItem(models.Model):
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING, null=True)
    leverings_datum = models.DateField(auto_now_add=True)
    leverancier = models.ForeignKey("directie.Leverancier", on_delete=models.DO_NOTHING, null=True)
    houdsbaarheiddatum = models.DateField()
    status = models.IntegerField()
    