from django.urls import path

from .views import  FincaCreateView, FincaListView


urlpatterns = [
    path('finca/add', FincaCreateView.as_view(), name="finca_create"),
    path("finca/",  FincaListView.as_view(), name="finca_list"),
]