from django.db import models

# Create your models here.
class ProductItem(models.Model):

    STATUS_CHOICES = (
        (1, 'Goed'),
        (2, 'Beschadigd'),
        (3, 'Verlopen'),
        (4, 'Verdwenen'),
    )

    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING, null=True)
    leverings_datum = models.DateField(auto_now_add=True)
    leverancier = models.ForeignKey("directie.Leverancier", on_delete=models.DO_NOTHING, null=True)
    houdsbaarheiddatum = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.product} {self.leverancier}"
    