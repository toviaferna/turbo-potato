from django.urls import path

from .views import  FincaCreateView, FincaListView,FincaUpdateView,FincaDeleteView


urlpatterns = [
    path('finca/<int:pk>/delete/', FincaDeleteView.as_view(), name="finca_delete"),
    path('finca/<int:pk>/update/', FincaUpdateView.as_view(), name="finca_update"),
    path('finca/add', FincaCreateView.as_view(), name="finca_create"),
    path("finca/",  FincaListView.as_view(), name="finca_list"),
]