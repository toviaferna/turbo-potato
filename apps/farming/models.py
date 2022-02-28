from django.db import models

class Finca(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    dimensionHa = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Dimension Ha")
    ubicacion = models.CharField(max_length=200,verbose_name="Ubicacion")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion
