from apps.reports import views
from django.urls import path

urlpatterns = [
    path(
        "informe-compra/", views.CompraInformeListView.as_view(), name="informe_compra_list",
    ),
    path(
        "informe-venta/", views.VentaInformeListView.as_view(), name="informe_venta_list",
    ),
    path(        
        "informe-actividad-agricola/", views.ProduccionAgricolaInformeListView.as_view(), name="informe_actividad_agricola_list",
    ),
    path(
        "informe-inventario-deposito/", views.InventarioDepositoInformeListView.as_view(), name="informe_inventario_deposito_list",
    ),
]
