from apps.inventory import views
from django.urls import path

urlpatterns = [
    path("marca/<int:pk>/delete/", views.MarcaDeleteView.as_view(), name="marca_delete"),
    path("marca/<int:pk>/update/", views.MarcaUpdateView.as_view(), name="marca_update"),
    path("marca/add", views.MarcaCreateView.as_view(), name="marca_create"),
    path("marca/",  views.MarcaListView.as_view(), name="marca_list"),
    path("deposito/<int:pk>/delete/", views.DepositoDeleteView.as_view(), name="deposito_delete"),
    path("deposito/<int:pk>/update/", views.DepositoUpdateView.as_view(), name="deposito_update"),
    path("deposito/add", views.DepositoCreateView.as_view(), name="deposito_create"),
    path("deposito/",  views.DepositoListView.as_view(), name="deposito_list"),
    path("categoria/<int:pk>/delete/", views.CategoriaDeleteView.as_view(), name="categoria_delete"),
    path("categoria/<int:pk>/update/", views.CategoriaUpdateView.as_view(), name="categoria_update"),
    path("categoria/add", views.CategoriaCreateView.as_view(), name="categoria_create"),
    path("categoria/",  views.CategoriaListView.as_view(), name="categoria_list"),
    #path("tipo-item/<int:pk>/delete/", views.TipoItemDeleteView.as_view(), name="tipo_item_delete"),
    #path("tipo-item/<int:pk>/update/", views.TipoItemUpdateView.as_view(), name="tipo_item_update"),
    #path("tipo-item/add", views.TipoItemCreateView.as_view(), name="tipo_item_create"),
    #path("tipo-item/",  views.TipoItemListView.as_view(), name="tipo_item_list"),
    path("item/<int:pk>/delete/", views.ItemDeleteView.as_view(), name="item_delete"),
    path("item/<int:pk>/update/", views.ItemUpdateView.as_view(), name="item_update"),
    path("item/add", views.ItemCreateView.as_view(), name="item_create"),
    path("item/",  views.ItemListView.as_view(), name="item_list"),
    path("ajuste-stock/<int:pk>/delete/", views.AjusteStockDeleteView.as_view(), name="ajuste_stock_delete"),
    path("ajuste-stock/<int:pk>/update/", views.AjusteStockUpdateView.as_view(), name="ajuste_stock_update"),
    path("ajuste-stock/add", views.AjusteStockCreateView.as_view(), name="ajuste_stock_create"),
    path("ajuste-stock/",  views.AjusteStockListView.as_view(), name="ajuste_stock_list"),
]
