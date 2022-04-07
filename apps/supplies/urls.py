from django.urls import path

from .views import (CompraAnnulledView, CompraCreateView, CompraDetailView,
                    CompraListView, OrdenCompraAnnulledView,
                    OrdenCompraCreateView, OrdenCompraListView,
                    PedidoCompraCreateView, PedidoCompraListView,
                    PedidoCompraUpdateView)

urlpatterns = [
    path('compra/<int:pk>/detail/', CompraDetailView.as_view(), name="compra_detail"),
    path('compra/<int:pk>/delete/', CompraAnnulledView.as_view(), name="compra_delete"),
    path('compra/add', CompraCreateView.as_view(), name="compra_create"),
    path("compra/",  CompraListView.as_view(), name="compra_list"),
    
    path('orden_compra/<int:pk>/delete/', OrdenCompraAnnulledView.as_view(), name="orden_compra_delete"),
    path('orden_compra/add', OrdenCompraCreateView.as_view(), name="orden_compra_create"),
    path("orden_compra/",  OrdenCompraListView.as_view(), name="orden_compra_list"),
    
    path('pedido_compra/<int:pk>/update/', PedidoCompraUpdateView.as_view(), name="pedido_compra_update"),
    path('pedido_compra/add', PedidoCompraCreateView.as_view(), name="pedido_compra_create"),
    path("pedido_compra/",  PedidoCompraListView.as_view(), name="pedido_compra_list"),
]
