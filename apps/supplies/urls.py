from django.urls import path

from .views import OrdenCompraCreateView, OrdenCompraListView, OrdenCompraAnnulledView, PedidoCompraCreateView, PedidoCompraListView, PedidoCompraUpdateView 

urlpatterns = [
    path('orden_compra/<int:pk>/delete/', OrdenCompraAnnulledView.as_view(), name="orden_compra_delete"),
    path('orden_compra/add', OrdenCompraCreateView.as_view(), name="orden_compra_create"),
    path("orden_compra/",  OrdenCompraListView.as_view(), name="orden_compra_list"),
    
    path('pedido_compra/<int:pk>/update/', PedidoCompraUpdateView.as_view(), name="pedido_compra_update"),
    path('pedido_compra/add', PedidoCompraCreateView.as_view(), name="pedido_compra_create"),
    path("pedido_compra/",  PedidoCompraListView.as_view(), name="pedido_compra_list"),
]