from django.db import models

class Finca(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripción",unique=True)
    dimensionHa = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Dimension Ha")
    ubicacion = models.CharField(max_length=200,verbose_name="Ubicacion")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class TipoActividadAgricola(models.Model):
    #  error_messages={'unique': u'My custom message'}
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion",unique=True)
    esCosecha = models.BooleanField(verbose_name="es Cosecha")
    esSiembra = models.BooleanField(verbose_name="es Siembra")
    esResiembra = models.BooleanField(verbose_name="es Resiembra")
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
    kgEstimado = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Kg Estimado")
    esZafrinha = models.BooleanField(verbose_name="Es Zafriña?")
    estaCerrado = models.BooleanField(verbose_name="Está Cerrado?",default=False)
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
    tipoMaquinariaAgricola = models.ForeignKey(TipoMaquinariaAgricola, on_delete=models.DO_NOTHING, verbose_name="Maquinaria Agrícola Tipo")
    esImplemento = models.BooleanField(verbose_name="Es Implemento?")
    admiteImplemento = models.BooleanField(verbose_name="Admite Implemento?")
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
    planActividadZafra = models.ForeignKey(PlanActividadZafra, on_delete=models.DO_NOTHING)
    fechaActividad = models.DateField(verbose_name="Fecha Act.")
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING,verbose_name="Finca")
    tipoActividadAgricola = models.ForeignKey(TipoActividadAgricola, on_delete=models.DO_NOTHING, null=True, blank=True,verbose_name="Tipo Actividad Agrícola")
    descripcion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Descripción")
    costo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo Estimado")

class Acopio(models.Model):
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Depósito")
    conductor = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Conductor")
    camion = models.ForeignKey(MaquinariaAgricola, on_delete=models.DO_NOTHING,verbose_name="Camión")
    fecha = models.DateField(verbose_name="Fecha")
    comprobante = models.CharField(max_length=30,verbose_name="Comprobante")
    pBruto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso Bruto",default=0)
    pTara = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso Tara",default=0)
    pDescuento = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso Desc.",default=0)
    pBonificacion = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso Bonif.",default=0)
    esTransportadoraPropia = models.BooleanField(verbose_name="Es Transportadora Propia?",default=False)
    esVigente = models.BooleanField(verbose_name="Vigente?",default=True)
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    @property
    def total(self):
        pesoBru = self.pBruto
        pesoBon = self.pBonificacion
        pesoTara = self.pTara
        pesoDesc = self.pDescuento
        if pesoBru is None :
            pesoBru = 0
        if pesoBon is None :
            pesoBon = 0
        if pesoTara is None :
            pesoTara = 0
        if pesoDesc is None :
            pesoDesc = 0
        return (pesoBru + pesoBon) - (pesoTara + pesoDesc)

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
    calificacionAgricola = models.ForeignKey(CalificacionAgricola, on_delete=models.DO_NOTHING,verbose_name="Calif. Agrícola")
    grado = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Grado")
    porcentaje = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Porcentaje")
    peso = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Peso")

class ActividadAgricola(models.Model):
    tipoActividadAgricola = models.ForeignKey(TipoActividadAgricola, on_delete=models.DO_NOTHING,verbose_name="Tipo Act. Agrícola")
    lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING,verbose_name="Lote")
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING,verbose_name="Finca")
    fechaDocumento = models.DateField(verbose_name="Fecha")
    empleado = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Empleado")
    fechaHoraRegistro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    esVigente = models.BooleanField(verbose_name="Vigente?",default=True)
    esServicioContratado = models.BooleanField(verbose_name="Es contratado?",default=False)
    cantidadTrabajada = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="HA Trabajada")
    @property
    def totalMaquinaria(self):
        retorno = sum(round(x.precio * x.haTrabajada)  for x in self.actividadagricolamaquinariadetalle_set.all())
        if retorno is None:
            retorno = 0
        return retorno
    @property    
    def totalItem(self):
        retorno = sum(round(x.costo * x.cantidad)  for x in self.actividadagricolaitemdetalle_set.all())
        if retorno is None:
            retorno = 0
        return retorno
    @property    
    def total(self):
        maquinaria = self.totalMaquinaria
        item = self.totalItem
        if maquinaria is None: 
           maquinaria = 0
        if item is None: 
            item = 0
        return maquinaria + item 

class ActividadAgricolaMaquinariaDetalle(models.Model):
    actividadAgricola = models.ForeignKey(ActividadAgricola, on_delete=models.DO_NOTHING)
    maquinaria = models.ForeignKey(MaquinariaAgricola, on_delete=models.DO_NOTHING,verbose_name="Maquinaria")
    haTrabajada = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Ha Trabajada")
    precio = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Precio HA")

class ActividadAgricolaItemDetalle(models.Model):
    actividadAgricola = models.ForeignKey(ActividadAgricola, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,verbose_name="Item")
    costo = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    porcentajeImpuesto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="% Impuesto")
    dosis = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Dosis")
    deposito = models.ForeignKey(Deposito, on_delete=models.DO_NOTHING,verbose_name="Deposito",default=1)


class Contrato(models.Model):
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Persona")
    costoPactado = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Precio Pactado")
    fecha = models.DateField(verbose_name="Fecha")
    descripcion = models.CharField(max_length=300,verbose_name="Descripción")

class LiquidacionAgricola(models.Model):
    VALORESENUMTIPMOV = (
    ('ACOPIOS', 'LIQUIDACION DE ACOPIOS'),
    ('ACTIVIDADES AGRICOLAS', 'LIQUIDACION DE ACTIVIDADES AGRICOLAS'),
    )
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    fechaDocumento = models.DateField(verbose_name="Fecha")
    proveedor = models.ForeignKey(Persona, on_delete=models.DO_NOTHING,verbose_name="Proveedor")
    fechaHoraRegistro = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Hora Registro")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    esVigente = models.BooleanField(verbose_name="Vigente?",default=True)
    precioUnitario = models.DecimalField(max_digits=15, decimal_places=0,verbose_name="Precio")
    tipo = models.CharField(max_length=50,choices=VALORESENUMTIPMOV,verbose_name="Tipo Liquidación") 
    @property
    def total(self):
        return sum(round(self.precioUnitario * x.cantidad)  for x in self.liquidacionagricoladetalle_set.all())
        
class LiquidacionAgricolaDetalle(models.Model):
    liquidacionAgricola = models.ForeignKey(LiquidacionAgricola, on_delete=models.DO_NOTHING)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Cantidad")
    lote = models.ForeignKey(Lote, on_delete=models.DO_NOTHING,verbose_name="Lote")
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING,verbose_name="Finca")
    secuenciaOrigen = models.IntegerField()

class CierreZafra(models.Model):
    zafra = models.ForeignKey(Zafra, on_delete=models.DO_NOTHING,verbose_name="Zafra")
    fecha = models.DateField(verbose_name="Fecha")
    observacion = models.CharField(max_length=300, null=True, blank=True,verbose_name="Observación")
    @property
    def totalCosto(self):
        return sum(round(x.costoTotal)  for x in self.cierrezafradetalle_set.all())
    @property
    def totalCultivado(self):
        return sum(round(x.haCultivada)  for x in self.cierrezafradetalle_set.all())
    @property
    def totalAcopiado(self):
        return sum(round(x.cantidadAcopioNeto)  for x in self.cierrezafradetalle_set.all())
    @property
    def totalHA(self):
        return sum(round(x.haCultivada)  for x in self.cierrezafradetalle_set.all())
    @property
    def totalCostoHa(self):
        return round(self.totalCosto / self.totalHA)
    @property
    def totalCostoUnit(self):
        return round(self.totalCosto / self.totalAcopiado)
    def __str__(self):
        return self.zafra.descripcion

class CierreZafraDetalle(models.Model):
    cierreZafra = models.ForeignKey(CierreZafra, on_delete=models.CASCADE)
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING,verbose_name="Finca")
    haCultivada = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="HA Cultivada")
    cantidadAcopioNeto = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="KG Acopiado")
    rendimiento = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Rendimiento")
    costoTotal = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo Total")
    costoHA = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo HA")
    costoUnit = models.DecimalField(max_digits=15, decimal_places=2,verbose_name="Costo Unit.")