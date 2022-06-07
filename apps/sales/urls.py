from django.urls import path

from apps.sales.views import AperturaCajaListView


urlpatterns = [
    #path('finca/<int:pk>/delete/', FincaDeleteView.as_view(), name="finca_delete"),
    #path('finca/<int:pk>/update/', FincaUpdateView.as_view(), name="finca_update"),
    #path('finca/add', FincaCreateView.as_view(), name="finca_create"),
    path("apertura-caja/",  AperturaCajaListView.as_view(), name="apertura_caja_list"),
]