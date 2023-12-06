from django.db import models

# Create your models here.
class ProductItem(models.Model):

    STATUS_CHOICES = (
        (1, 'Goed'),
        (2, 'in pakket'),
        (3, 'Verlopen'),
        (4, 'Verdwenen'),
    )

    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, related_name="product_items")
    leverings_datum = models.DateField(auto_now_add=True)
    leverancier = models.ForeignKey("directie.Leverancier", on_delete=models.SET_NULL, null=True, related_name="product_items")
    houdsbaarheiddatum = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    pakket = models.ForeignKey("magazijn.Pakket", on_delete=models.SET_NULL, null=True, blank=True, related_name="product_items")

    def __str__(self):
        if self.product:
            return f"{self.product.name} {self.leverancier} .'houdbaarheidsdatum ->'.{self.houdsbaarheiddatum}"
        else:
            return f"{'geen product'} {self.leverancier} {self.houdsbaarheiddatum}"
    