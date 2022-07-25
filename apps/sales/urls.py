from apps.sales import views
from django.urls import path

urlpatterns = [
    path("apertura-caja/",  views.AperturaCajaListView.as_view(), name="apertura_caja_list"),
    path("apertura-caja/add", views.AperturaCajaCreateView.as_view(), name="apertura_caja_create"),
    path("apertura-caja/<int:pk>/cerrar", views.AperturaCajaDeleteView.as_view(), name="apertura_caja_delete"),
    path("arqueo/",  views.ArqueoListView.as_view(), name="arqueo_list"),
    path("arqueo/add", views.ArqueoCreateView.as_view(), name="arqueo_create"),
    path("arqueo/<int:pk>/cerrar", views.ArqueoDeleteView.as_view(), name="arqueo_delete"),
    path('transferencia-cuenta/<int:pk>/delete',views.TransferenciaCuentaAnnulledView.as_view(), name="transferencia_cuenta_delete"),
    path('transferencia-cuenta/add',views.TransferenciaCuentaCreateView.as_view(), name="transferencia_cuenta_create"),
    path('transferencia-cuenta', views.TransferenciaCuentaListView.as_view(), name="transferencia_cuenta_list"),
    path('venta/<int:pk>/delete',views.VentaAnnulledView.as_view(), name="venta_delete"),
    path('venta/<int:pk>/download',views.download_view, name="venta_download"),
    path('venta/add',views.VentaCreateView.as_view(), name="venta_create"),
    path('venta', views.VentaListView.as_view(), name="venta_list"),
    path('nota-credito-emitida/<int:pk>/delete',views.NotaCreditoEmitidaAnnulledView.as_view(), name="nota_credito_emitida_delete"),
    path('nota-credito-emitida/add',views.NotaCreditoEmitidaCreateView.as_view(), name="nota_credito_emitida_create"),
    path('nota-credito-emitida', views.NotaCreditoEmitidaListView.as_view(), name="nota_credito_emitida_list"),
    path('nota-debito-emitida/<int:pk>/delete',views.NotaDebitoEmitidaAnnulledView.as_view(), name="nota_debito_emitida_delete"),
    path('nota-debito-emitida/add',views.NotaDebitoEmitidaCreateView.as_view(), name="nota_debito_emitida_create"),
    path('nota-debito-emitida', views.NotaDebitoEmitidaListView.as_view(), name="nota_debito_emitida_list"),
    path('cobro/<int:pk>/delete', views.CobroAnnulledView.as_view(), name="cobro_delete"),
    path('cobro/add', views.CobroCreateView.as_view(), name="cobro_create"),
    path('cobro/selection', views.CobroPersonaSelectionListView.as_view(), name="cobro_selection"),
    path('cobro', views.CobroListView.as_view(), name="cobro_list"),
]
