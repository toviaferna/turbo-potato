from django.urls import path

from .views import (CompraAnnulledView, CompraCreateView, CompraDetailView,
                    CompraListView, LibroCompraListView, NotaCreditoRecibidaAnnulledView, NotaCreditoRecibidaCreateView, NotaCreditoRecibidaListView, NotaDebitoRecibidaAnnulledView, NotaDebitoRecibidaCreateView, NotaDebitoRecibidaListView, OrdenCompraAnnulledView,
                    OrdenCompraCreateView, OrdenCompraListView,
                    PedidoCompraCreateView, PedidoCompraListView,
                    PedidoCompraUpdateView)

urlpatterns = [
    path("libro-compra/",  LibroCompraListView.as_view(), name="libro_compra_list"),

    path('compra/<int:pk>/detail/', CompraDetailView.as_view(), name="compra_detail"),
    path('compra/<int:pk>/delete/', CompraAnnulledView.as_view(), name="compra_delete"),
    path('compra/add', CompraCreateView.as_view(), name="compra_create"),
    path("compra/",  CompraListView.as_view(), name="compra_list"),

    path('nota-credito-recibida/<int:pk>/delete/', NotaCreditoRecibidaAnnulledView.as_view(), name="nota_credito_recibida_delete"),
    path('nota-credito-recibida/add', NotaCreditoRecibidaCreateView.as_view(), name="nota_credito_recibida_create"),
    path("nota-credito-recibida/",  NotaCreditoRecibidaListView.as_view(), name="nota_credito_recibida_list"),
    
    path('nota-debito-recibida/<int:pk>/delete/', NotaDebitoRecibidaAnnulledView.as_view(), name="nota_debito_recibida_delete"),
    path('nota-debito-recibida/add', NotaDebitoRecibidaCreateView.as_view(), name="nota_debito_recibida_create"),
    path("nota-debito-recibida/",  NotaDebitoRecibidaListView.as_view(), name="nota_debito_recibida_list"),
    
    path('orden-compra/<int:pk>/delete/', OrdenCompraAnnulledView.as_view(), name="orden_compra_delete"),
    path('orden-compra/add', OrdenCompraCreateView.as_view(), name="orden_compra_create"),
    path("orden-compra/",  OrdenCompraListView.as_view(), name="orden_compra_list"),
    
    path('pedido-compra/<int:pk>/update/', PedidoCompraUpdateView.as_view(), name="pedido_compra_update"),
    path('pedido-compra/add', PedidoCompraCreateView.as_view(), name="pedido_compra_create"),
    path("pedido-compra/",  PedidoCompraListView.as_view(), name="pedido_compra_list"),
]
