from django.urls import path

from .views import  FincaListView


urlpatterns = [
    path("finca/",  FincaListView.as_view(), name="finca_list"),
]