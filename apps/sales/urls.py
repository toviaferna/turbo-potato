from apps.sales import views
from django.urls import path

urlpatterns = [
    path("apertura-caja/",  views.AperturaCajaListView.as_view(), name="apertura_caja_list"),
    path("apertura-caja/add", views.AperturaCajaCreateView.as_view(), name="apertura_caja_create"),
    path("apertura-caja/<int:pk>/cerrar", views.AperturaCajaDeleteView.as_view(), name="apertura_caja_delete"),
    path("arqueo/",  views.ArqueoListView.as_view(), name="arqueo_list"),
    path("arqueo/add", views.ArqueoCreateView.as_view(), name="arqueo_create"),
    path("arqueo/<int:pk>/cerrar", views.ArqueoDeleteView.as_view(), name="arqueo_delete"),
    path('transferencia_cuenta/<int:pk>/delete',views.TransferenciaCuentaAnnulledView.as_view(), name="transferencia_cuenta_delete"),
    path('transferencia_cuenta/add',views.TransferenciaCuentaCreateView.as_view(), name="transferencia_cuenta_create"),
    path('transferencia_cuenta', views.TransferenciaCuentaListView.as_view(), name="transferencia_cuenta_list"),
    #path('venta/<int:pk>/delete',views.VentaAnularView.as_view(), name="venta_delete"),
    #path('venta/<int:pk>/download',views.download_view, name="venta_download"),
    path('venta/add',views.VentaCreateView.as_view(), name="venta_create"),
    path('venta', views.VentaListView.as_view(), name="venta_list"),
]
