from django.urls import path

from .views import  MarcaCreateView, MarcaListView,MarcaUpdateView, MarcaDeleteView

urlpatterns = [
    path('marca/<int:pk>/delete/', MarcaDeleteView.as_view(), name="marca_delete"),
    path('marca/<int:pk>/update/', MarcaUpdateView.as_view(), name="marca_update"),
    path('marca/add', MarcaCreateView.as_view(), name="marca_create"),
    path("marca/",  MarcaListView.as_view(), name="marca_list"),
]