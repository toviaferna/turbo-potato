from django.db import models

# Create your models here.
class Marca(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion