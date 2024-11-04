from django.urls import path

from apps.sales import views

urlpatterns = [
    path(
        "apertura-caja/",
        views.AperturaCajaListView.as_view(),
        name="apertura_caja_list",
    ),
    path(
        "apertura-caja/add",
        views.AperturaCajaCreateView.as_view(),
        name="apertura_caja_create",
    ),
    path(
        "apertura-caja/<int:pk>/cerrar",
        views.AperturaCajaDeleteView.as_view(),
        name="apertura_caja_delete",
    ),
    path("arqueo/", views.ArqueoListView.as_view(), name="arqueo_list"),
    path("arqueo/add", views.ArqueoCreateView.as_view(), name="arqueo_create"),
    path(
        "arqueo/<int:pk>/cerrar", views.ArqueoDeleteView.as_view(), name="arqueo_delete"
    ),
    path(
        "transferencia-cuenta/<int:pk>/delete",
        views.TransferenciaCuentaAnnulledView.as_view(),
        name="transferencia_cuenta_delete",
    ),
    path(
        "transferencia-cuenta/add",
        views.TransferenciaCuentaCreateView.as_view(),
        name="transferencia_cuenta_create",
    ),
    path(
        "transferencia-cuenta",
        views.TransferenciaCuentaListView.as_view(),
        name="transferencia_cuenta_list",
    ),
    path(
        "venta/<int:pk>/detail/",
        views.VentaDetailView.as_view(),
        name="venta_detail",
    ),
    path(
        "venta/<int:pk>/delete", views.VentaAnnulledView.as_view(), name="venta_delete"
    ),
    path("venta/<int:pk>/download", views.download_view, name="venta_download"),
    path("venta/add", views.VentaCreateView.as_view(), name="venta_create"),
    path("venta", views.VentaListView.as_view(), name="venta_list"),
    path(
        "nota-credito-emitida/<int:pk>/detail/",
        views.NotaCreditoEmitidaDetailView.as_view(),
        name="nota_credito_emitida_detail",
    ),
    path(
        "nota-credito-emitida/<int:pk>/delete",
        views.NotaCreditoEmitidaAnnulledView.as_view(),
        name="nota_credito_emitida_delete",
    ),
    path(
        "nota-credito-emitida/add",
        views.NotaCreditoEmitidaCreateView.as_view(),
        name="nota_credito_emitida_create",
    ),
    path(
        "nota-credito-emitida",
        views.NotaCreditoEmitidaListView.as_view(),
        name="nota_credito_emitida_list",
    ),
    path(
        "nota-debito-emitida/<int:pk>/detail/",
        views.NotaDebitoEmitidaDetailView.as_view(),
        name="nota_debito_emitida_detail",
    ),
    path(
        "nota-debito-emitida/<int:pk>/delete",
        views.NotaDebitoEmitidaAnnulledView.as_view(),
        name="nota_debito_emitida_delete",
    ),
    path(
        "nota-debito-emitida/add",
        views.NotaDebitoEmitidaCreateView.as_view(),
        name="nota_debito_emitida_create",
    ),
    path(
        "nota-debito-emitida",
        views.NotaDebitoEmitidaListView.as_view(),
        name="nota_debito_emitida_list",
    ),
    path(
        "cobro/<int:pk>/delete", views.CobroAnnulledView.as_view(), name="cobro_delete"
    ),
    path("cobro/add", views.CobroCreateView.as_view(), name="cobro_create"),
    path(
        "cobro/selection",
        views.CobroPersonaSelectionListView.as_view(),
        name="cobro_selection",
    ),
    path("cobro", views.CobroListView.as_view(), name="cobro_list"),
    path("libro-venta", views.LibroVentaListView.as_view(), name="libro_venta_list"),
    
    path("establecimiento/<int:pk>/delete/", views.EstablecimientoDeleteView.as_view(), name="establecimiento_delete"),
    path("establecimiento/<int:pk>/update/", views.EstablecimientoUpdateView.as_view(), name="establecimiento_update"),
    path("establecimiento/add", views.EstablecimientoCreateView.as_view(), name="establecimiento_create"),
    path("establecimiento/",  views.EstablecimientoListView.as_view(), name="establecimiento_list"),
    path("punto-expedicion/<int:pk>/delete/", views.PuntoExpedicionDeleteView.as_view(), name="punto_expedicion_delete"),
    path("punto-expedicion/<int:pk>/update/", views.PuntoExpedicionUpdateView.as_view(), name="punto_expedicion_update"),
    path("punto-expedicion/add", views.PuntoExpedicionCreateView.as_view(), name="punto_expedicion_create"),
    path("punto-expedicion/",  views.PuntoExpedicionListView.as_view(), name="punto_expedicion_list"),
    path("tipo-documento/<int:pk>/delete/", views.TipoDocumentoDeleteView.as_view(), name="tipo_documento_delete"),
    path("tipo-documento/<int:pk>/update/", views.TipoDocumentoUpdateView.as_view(), name="tipo_documento_update"),
    path("tipo-documento/add", views.TipoDocumentoCreateView.as_view(), name="tipo_documento_create"),
    path("tipo-documento/",  views.TipoDocumentoListView.as_view(), name="tipo_documento_list"),
    path("timbrado/<int:pk>/delete/", views.TimbradoDeleteView.as_view(), name="timbrado_delete"),
    path("timbrado/<int:pk>/update/", views.TimbradoUpdateView.as_view(), name="timbrado_update"),
    path("timbrado/add", views.TimbradoCreateView.as_view(), name="timbrado_create"),
    path("timbrado/",  views.TimbradoListView.as_view(), name="timbrado_list"),
]
