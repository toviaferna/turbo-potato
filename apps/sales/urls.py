from apps.sales import views
from django.urls import path

urlpatterns = [
    path("apertura-caja/",  views.AperturaCajaListView.as_view(), name="apertura_caja_list"),
    path("apertura-caja/add", views.AperturaCajaCreateView.as_view(), name="apertura_caja_create"),
    path("apertura-caja/<int:pk>/cerrar", views.AperturaCajaDeleteView.as_view(), name="apertura_caja_delete"),
]
