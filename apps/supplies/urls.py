from django.urls import path

from .views import PedidoCompraListView #PedidoCompraCreateView, PedidoCompraListView,PedidoCompraUpdateView,PedidoCompraDeleteView


urlpatterns = [
    #path('pedido_compra/<int:pk>/delete/', PedidoCompraDeleteView.as_view(), name="pedido_compra_delete"),
    #path('pedido_compra/<int:pk>/update/', PedidoCompraUpdateView.as_view(), name="pedido_compra_update"),
    #path('pedido_compra/add', PedidoCompraCreateView.as_view(), name="pedido_compra_create"),
    path("pedido_compra/",  PedidoCompraListView.as_view(), name="pedido_compra_list"),
]