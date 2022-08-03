from apps.supplies import views
from django.urls import path

urlpatterns = [
    path(
        "libro-compra/", views.LibroCompraListView.as_view(), name="libro_compra_list"
    ),
    path(
        "compra/<int:pk>/detail/",
        views.CompraDetailView.as_view(),
        name="compra_detail",
    ),
    path(
        "compra/<int:pk>/delete/",
        views.CompraAnnulledView.as_view(),
        name="compra_delete",
    ),
    path("compra/add", views.CompraCreateView.as_view(), name="compra_create"),
    path("compra/", views.CompraListView.as_view(), name="compra_list"),
    path(
        "nota-credito-recibida/<int:pk>/delete/",
        views.NotaCreditoRecibidaAnnulledView.as_view(),
        name="nota_credito_recibida_delete",
    ),
    path(
        "nota-credito-recibida/add",
        views.NotaCreditoRecibidaCreateView.as_view(),
        name="nota_credito_recibida_create",
    ),
    path(
        "nota-credito-recibida/",
        views.NotaCreditoRecibidaListView.as_view(),
        name="nota_credito_recibida_list",
    ),
    path(
        "nota-debito-recibida/<int:pk>/delete/",
        views.NotaDebitoRecibidaAnnulledView.as_view(),
        name="nota_debito_recibida_delete",
    ),
    path(
        "nota-debito-recibida/add",
        views.NotaDebitoRecibidaCreateView.as_view(),
        name="nota_debito_recibida_create",
    ),
    path(
        "nota-debito-recibida/",
        views.NotaDebitoRecibidaListView.as_view(),
        name="nota_debito_recibida_list",
    ),
    path(
        "orden-compra/<int:pk>/delete/",
        views.OrdenCompraAnnulledView.as_view(),
        name="orden_compra_delete",
    ),
    path(
        "orden-compra/add",
        views.OrdenCompraCreateView.as_view(),
        name="orden_compra_create",
    ),
    path(
        "orden-compra/", views.OrdenCompraListView.as_view(), name="orden_compra_list"
    ),
    path(
        "pedido-compra/<int:pk>/update/",
        views.PedidoCompraUpdateView.as_view(),
        name="pedido_compra_update",
    ),
    path(
        "pedido-compra/add",
        views.PedidoCompraCreateView.as_view(),
        name="pedido_compra_create",
    ),
    path(
        "pedido-compra/",
        views.PedidoCompraListView.as_view(),
        name="pedido_compra_list",
    ),
]
