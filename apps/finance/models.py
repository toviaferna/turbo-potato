from django.db import models

# Create your models here.


class TipoImpuesto(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="% Impuesto")
    es_iva = models.BooleanField(max_length=200,verbose_name="es IVA?")
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Tipo de impuesto"
        verbose_name_plural = "Tipos de impuestos"
   
    def __str__(self):
        return self.descripcion
        
class Banco(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    
    def __str__(self):
        return self.descripcion
    
class Cuenta(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    es_banco = models.BooleanField(verbose_name="Es Banco?",default=False)
    nro_cuenta = models.CharField(max_length=200, verbose_name="Nro Cuenta",null=True,blank=True)
    banco = models.ForeignKey(Banco, on_delete=models.DO_NOTHING, verbose_name="Banco",null=True,blank=True)
    
    def __str__(self):
        return self.descripcion
class Pais(models.Model):
    abreviatura = models.CharField(max_length=200, verbose_name="Abreviatura",unique=True)
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    
    class Meta:
        verbose_name_plural = "Paises"
    
    def __str__(self):
        return self.descripcion

class Departamento(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)

    def __str__(self):
        return self.descripcion

class Distrito(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, verbose_name="Departamento")
    
    def __str__(self):
        return self.descripcion

class Localidad(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")
    distrito = models.ForeignKey(Distrito, on_delete=models.DO_NOTHING, verbose_name="Distrito")
    
    class Meta:
        verbose_name_plural = "Localidades"
    
    def __str__(self):
        return f"{self.descripcion}"

class Persona(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, verbose_name="Pais")
    localidad = models.ForeignKey(Localidad, on_delete=models.DO_NOTHING, verbose_name="Localidad")
    razon_social = models.CharField(max_length=200, verbose_name="Razon Social")
    documento = models.CharField(max_length=40, verbose_name="Documento")
    direccion = models.CharField(max_length=200, verbose_name="Direccion")
    celular = models.CharField(max_length=60, verbose_name="Celular / Telefono",null=True,blank=True)
    es_cliente = models.BooleanField(verbose_name="Es Cliente?",default=False,help_text="La persona será tratada como un cliente")
    es_proveedor = models.BooleanField(verbose_name="Es Proveedor?",default=False,help_text="La persona será tratada como un proveedor")
    es_empleado = models.BooleanField(verbose_name="Es Empleado?",default=False,help_text="La persona será tratada como un empleado de la empresa")


    def __str__(self):
        return self.razon_social
