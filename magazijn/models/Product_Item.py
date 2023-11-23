from django.db import models

# Create your models here.
class ProductItem(models.Model):

    STATUS_CHOICES = (
        (1, 'Goed'),
        (2, 'in pakket'),
        (3, 'Verlopen'),
        (4, 'Verdwenen'),
    )

    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    leverings_datum = models.DateField(auto_now_add=True)
    leverancier = models.ForeignKey("directie.Leverancier", on_delete=models.SET_NULL, null=True)
    houdsbaarheiddatum = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    pakket = models.ForeignKey("magazijn.Pakket", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if self.product:
            return f"{self.product.name} {self.leverancier} {self.houdsbaarheiddatum}"
        else:
            return f"{'geen product'} {self.leverancier} {self.houdsbaarheiddatum}"
    