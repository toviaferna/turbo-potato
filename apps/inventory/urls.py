from django.urls import path

from .views import (AjusteStockCreateView, AjusteStockDeleteView, AjusteStockListView, AjusteStockUpdateView, CategoriaCreateView, CategoriaDeleteView,
                    CategoriaListView, CategoriaUpdateView, DepositoCreateView,
                    DepositoDeleteView, DepositoListView, DepositoUpdateView, ItemCreateView, ItemDeleteView, ItemListView, ItemUpdateView,
                    MarcaCreateView, MarcaDeleteView, MarcaListView,
                    MarcaUpdateView, TipoItemCreateView, TipoItemDeleteView,
                    TipoItemListView, TipoItemUpdateView)

urlpatterns = [
    path('marca/<int:pk>/delete/', MarcaDeleteView.as_view(), name="marca_delete"),
    path('marca/<int:pk>/update/', MarcaUpdateView.as_view(), name="marca_update"),
    path('marca/add', MarcaCreateView.as_view(), name="marca_create"),
    path("marca/",  MarcaListView.as_view(), name="marca_list"),
    path('deposito/<int:pk>/delete/', DepositoDeleteView.as_view(), name="deposito_delete"),
    path('deposito/<int:pk>/update/', DepositoUpdateView.as_view(), name="deposito_update"),
    path('deposito/add', DepositoCreateView.as_view(), name="deposito_create"),
    path("deposito/",  DepositoListView.as_view(), name="deposito_list"),
    path('categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name="categoria_delete"),
    path('categoria/<int:pk>/update/', CategoriaUpdateView.as_view(), name="categoria_update"),
    path('categoria/add', CategoriaCreateView.as_view(), name="categoria_create"),
    path("categoria/",  CategoriaListView.as_view(), name="categoria_list"),
    #path('tipo-item/<int:pk>/delete/', TipoItemDeleteView.as_view(), name="tipo_item_delete"),
    #path('tipo-item/<int:pk>/update/', TipoItemUpdateView.as_view(), name="tipo_item_update"),
    #path('tipo-item/add', TipoItemCreateView.as_view(), name="tipo_item_create"),
    #path("tipo-item/",  TipoItemListView.as_view(), name="tipo_item_list"),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name="item_delete"),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name="item_update"),
    path('item/add', ItemCreateView.as_view(), name="item_create"),
    path("item/",  ItemListView.as_view(), name="item_list"),
    path('ajuste-stock/<int:pk>/delete/', AjusteStockDeleteView.as_view(), name="ajuste_stock_delete"),
    path('ajuste-stock/<int:pk>/update/', AjusteStockUpdateView.as_view(), name="ajuste_stock_update"),
    path('ajuste-stock/add', AjusteStockCreateView.as_view(), name="ajuste_stock_create"),
    path("ajuste-stock/",  AjusteStockListView.as_view(), name="ajuste_stock_list"),
]
