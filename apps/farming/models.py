from django.db import models
from apps.finance.models import Persona

from apps.inventory.models import Deposito, Item

class Finca(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripción",unique=True)
    dimension_ha = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Dimension Ha")
    ubicacion = models.CharField(max_length=200,verbose_name="Ubicacion")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class TipoActividadAgricola(models.Model):
    #  error_messages={'unique': u'My custom message'}
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    es_cosecha = models.BooleanField(verbose_name="es Cosecha")
    es_siembra = models.BooleanField(verbose_name="es Siembra")
    es_resiembra = models.BooleanField(verbose_name="es Resiembra")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class TipoMaquinariaAgricola(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class Zafra(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, verbose_name="Item")
    anho = models.IntegerField(verbose_name="Anho")
    kg_estimado = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Kg Estimado")
    es_zafrinha = models.BooleanField(verbose_name="Es Zafriña?")
    esta_cerrado = models.BooleanField(verbose_name="Está Cerrado?",default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class Lote(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING, verbose_name="Zafra")
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING, verbose_name="Finca")
    dimension = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Dimensión HA")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.descripcion

class MaquinariaAgricola(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")
    tipo_maquinaria_agricola = models.ForeignKey(TipoMaquinariaAgricola, on_delete=models.DO_NOTHING, verbose_name="Maquinaria Agrícola Tipo")
    es_implemento = models.BooleanField(verbose_name="Es Implemento?")
    admite_implemento = models.BooleanField(verbose_name="Admite Implemento?")
    precio = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.descripcion

class PlanActividadZafra(models.Model):
    fecha = models.DateField(verbose_name="Fecha")
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING, null=True, blank=True,verbose_name="Zafra")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")

    @property
    def total(self):
        return sum(round(x.costo)  for x in self.planactividadzafradetalle_set.all())

class PlanActividadZafraDetalle(models.Model):
    plan_actividad_zafra = models.ForeignKey(PlanActividadZafra, on_delete=models.DO_NOTHING)
    fecha_actividad = models.DateField(verbose_name="Fecha Act.")
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING,verbose_name="Finca")
    tipo_actividad_agricola = models.ForeignKey(TipoActividadAgricola, on_delete=models.DO_NOTHING, null=True, blank=True,verbose_name="Tipo Actividad Agrícola")
    descripcion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Descripción")
    costo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo Estimado")

class Acopio(models.Model):
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Depósito")
    conductor = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Conductor")
    camion = models.ForeignKey(MaquinariaAgricola, on_delete=models.DO_NOTHING,verbose_name="Camión")
    fecha = models.DateField(verbose_name="Fecha")
    comprobante = models.CharField(max_length=30,verbose_name="Comprobante")
    peso_bruto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso Bruto",default=0)
    peso_tara = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso Tara",default=0)
    peso_descuento = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso Desc.",default=0)
    peso_bonificacion = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso Bonif.",default=0)
    es_transportadora_propia = models.BooleanField(verbose_name="Es Transportadora Propia?",default=False)
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    
    @property
    def total(self):
        peso_bruto = self.peso_bruto
        peso_bonificacion = self.peso_bonificacion
        peso_tara = self.peso_tara
        peso_descuento = self.peso_descuento
        
        if peso_bruto is None :
            peso_bruto = 0
        if peso_bonificacion is None :
            peso_bonificacion = 0
        if peso_tara is None :
            peso_tara = 0
        if peso_descuento is None :
            peso_descuento = 0
        return (peso_bruto + peso_bonificacion) - (peso_tara + peso_descuento)

class AcopioDetalle(models.Model):
    acopio = models.ForeignKey(Acopio, on_delete=models.DO_NOTHING)
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING,verbose_name="Finca")
    lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING,verbose_name="Lote")
    peso = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso")

class CalificacionAgricola(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    created = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.descripcion

class AcopioCalificacion(models.Model):
    acopio = models.ForeignKey(Acopio, on_delete=models.DO_NOTHING)
    calificacion_agricola = models.ForeignKey(CalificacionAgricola, on_delete=models.DO_NOTHING,verbose_name="Calif. Agrícola")
    grado = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Grado")
    porcentaje = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Porcentaje")
    peso = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso")

class ActividadAgricola(models.Model):
    tipo_actividad_agricola = models.ForeignKey(TipoActividadAgricola, on_delete=models.DO_NOTHING,verbose_name="Tipo Act. Agrícola")
    lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING,verbose_name="Lote")
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING,verbose_name="Finca")
    fecha_documento = models.DateField(verbose_name="Fecha")
    empleado = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Empleado")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    es_servicio_contratado = models.BooleanField(verbose_name="Es contratado?",default=False)
    cantidad_trabajada = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="HA Trabajada")
    
    @property
    def total_maquinaria(self):
        retorno = sum(round(x.precio * x.ha_trabajada)  for x in self.actividadagricolamaquinariadetalle_set.all())
        if retorno is None:
            retorno = 0
        return retorno

    @property    
    def total_item(self):
        retorno = sum(round(x.costo * x.cantidad)  for x in self.actividadagricolaitemdetalle_set.all())
        if retorno is None:
            retorno = 0
        return retorno

    @property    
    def total(self):
        maquinaria = self.total_maquinaria
        item = self.total_item
        if maquinaria is None: 
           maquinaria = 0
        if item is None: 
            item = 0
        return maquinaria + item 

class ActividadAgricolaMaquinariaDetalle(models.Model):
    actividad_agricola = models.ForeignKey(ActividadAgricola, on_delete=models.DO_NOTHING)
    maquinaria = models.ForeignKey(MaquinariaAgricola, on_delete=models.DO_NOTHING,verbose_name="Maquinaria")
    ha_trabajada = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Ha Trabajada")
    precio = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Precio HA")

class ActividadAgricolaItemDetalle(models.Model):
    actividad_agricola = models.ForeignKey(ActividadAgricola, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    costo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    porcentaje_impuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")
    dosis = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Dosis")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito",default=1)


class Contrato(models.Model):
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Persona")
    costo_pactado = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Precio Pactado")
    fecha = models.DateField(verbose_name="Fecha")
    descripcion = models.CharField(max_length=300,verbose_name="Descripción")

class LiquidacionAgricola(models.Model):
    VALORESENUMTIPMOV = (
        ('ACOPIOS', 'LIQUIDACION DE ACOPIOS'),
        ('ACTIVIDADES AGRICOLAS', 'LIQUIDACION DE ACTIVIDADES AGRICOLAS'),
    )
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    fecha_documento = models.DateField(verbose_name="Fecha")
    proveedor = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Proveedor")
    fecha_hora_registro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    es_vigente = models.BooleanField(verbose_name="Vigente?",default=True)
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=0,verbose_name="Precio")
    tipo = models.CharField(max_length=50,choices=VALORESENUMTIPMOV,verbose_name="Tipo Liquidación") 
    
    @property
    def total(self):
        return sum(round(self.precio_unitario * x.cantidad)  for x in self.liquidacionagricoladetalle_set.all())
        
class LiquidacionAgricolaDetalle(models.Model):
    liquidacion_agricola = models.ForeignKey(LiquidacionAgricola, on_delete=models.DO_NOTHING)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING,verbose_name="Lote")
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING,verbose_name="Finca")
    secuencia_origen = models.IntegerField()

class CierreZafra(models.Model):
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    fecha = models.DateField(verbose_name="Fecha")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    
    @property
    def total_costo(self):
        return sum(round(x.costo_total)  for x in self.cierrezafradetalle_set.all())
    
    @property
    def total_cultivado(self):
        return sum(round(x.ha_cultivada)  for x in self.cierrezafradetalle_set.all())
    
    @property
    def total_acopiado(self):
        return sum(round(x.cantidad_acopio_neto)  for x in self.cierrezafradetalle_set.all())
    
    @property
    def total_ha(self):
        return sum(round(x.ha_cultivada)  for x in self.cierrezafradetalle_set.all())
    
    @property
    def total_costo_ha(self):
        return round(self.total_costo / self.total_ha)

    @property
    def total_costo_unit(self):
        return round(self.total_costo / self.total_acopiado)

    def __str__(self):
        return self.zafra.descripcion

class CierreZafraDetalle(models.Model):
    cierre_zafra = models.ForeignKey(CierreZafra, on_delete=models.CASCADE)
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING,verbose_name="Finca")
    ha_cultivada = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="HA Cultivada")
    cantidad_acopio_neto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="KG Acopiado")
    rendimiento = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Rendimiento")
    costo_total = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo Total")
    costo_ha = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo HA")
    costo_unitario = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo Unit.")