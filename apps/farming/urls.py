from django.urls import path

from .views import  CalificacionAgricolaCreateView, CalificacionAgricolaDeleteView, CalificacionAgricolaListView, CalificacionAgricolaUpdateView, FincaCreateView, FincaListView,FincaUpdateView,FincaDeleteView, LoteCreateView, LoteDeleteView, LoteListView, LoteUpdateView, MaquinariaAgricolaCreateView, MaquinariaAgricolaDeleteView, MaquinariaAgricolaListView, MaquinariaAgricolaUpdateView, PlanActividadZafraCreateView, PlanActividadZafraListView, PlanActividadZafraUpdateView, TipoActividadAgricolaCreateView, TipoActividadAgricolaDeleteView, TipoActividadAgricolaListView, TipoActividadAgricolaUpdateView, TipoMaquinariaAgricolaCreateView, TipoMaquinariaAgricolaDeleteView, TipoMaquinariaAgricolaListView, TipoMaquinariaAgricolaUpdateView, ZafraCreateView, ZafraDeleteView, ZafraListView, ZafraUpdateView


urlpatterns = [
    path('finca/<int:pk>/delete/', FincaDeleteView.as_view(), name="finca_delete"),
    path('finca/<int:pk>/update/', FincaUpdateView.as_view(), name="finca_update"),
    path('finca/add', FincaCreateView.as_view(), name="finca_create"),
    path("finca/",  FincaListView.as_view(), name="finca_list"),
    path('calificacion-agricola/<int:pk>/delete/', CalificacionAgricolaDeleteView.as_view(), name="calificacion_agricola_delete"),
    path('calificacion-agricola/<int:pk>/update/', CalificacionAgricolaUpdateView.as_view(), name="calificacion_agricola_update"),
    path('calificacion-agricola/add', CalificacionAgricolaCreateView.as_view(), name="calificacion_agricola_create"),
    path("calificacion-agricola/",  CalificacionAgricolaListView.as_view(), name="calificacion_agricola_list"),
    path('tipo-actividad-agricola/<int:pk>/delete/', TipoActividadAgricolaDeleteView.as_view(), name="tipo_actividad_agricola_delete"),
    path('tipo-actividad-agricola/<int:pk>/update/', TipoActividadAgricolaUpdateView.as_view(), name="tipo_actividad_agricola_update"),
    path('tipo-actividad-agricola/add', TipoActividadAgricolaCreateView.as_view(), name="tipo_actividad_agricola_create"),
    path("tipo-actividad-agricola/",  TipoActividadAgricolaListView.as_view(), name="tipo_actividad_agricola_list"),
    path('tipo-maquinaria-agricola/<int:pk>/delete/', TipoMaquinariaAgricolaDeleteView.as_view(), name="tipo_maquinaria_agricola_delete"),
    path('tipo-maquinaria-agricola/<int:pk>/update/', TipoMaquinariaAgricolaUpdateView.as_view(), name="tipo_maquinaria_agricola_update"),
    path('tipo-maquinaria-agricola/add', TipoMaquinariaAgricolaCreateView.as_view(), name="tipo_maquinaria_agricola_create"),
    path("tipo-maquinaria-agricola/",  TipoMaquinariaAgricolaListView.as_view(), name="tipo_maquinaria_agricola_list"),
    path('maquinaria-agricola/<int:pk>/delete/', MaquinariaAgricolaDeleteView.as_view(), name="maquinaria_agricola_delete"),
    path('maquinaria-agricola/<int:pk>/update/', MaquinariaAgricolaUpdateView.as_view(), name="maquinaria_agricola_update"),
    path('maquinaria-agricola/add', MaquinariaAgricolaCreateView.as_view(), name="maquinaria_agricola_create"),
    path("maquinaria-agricola/",  MaquinariaAgricolaListView.as_view(), name="maquinaria_agricola_list"),
    path('zafra/<int:pk>/delete/', ZafraDeleteView.as_view(), name="zafra_delete"),
    path('zafra/<int:pk>/update/', ZafraUpdateView.as_view(), name="zafra_update"),
    path('zafra/add', ZafraCreateView.as_view(), name="zafra_create"),
    path("zafra/",  ZafraListView.as_view(), name="zafra_list"),
    path('lote/<int:pk>/delete/', LoteDeleteView.as_view(), name="lote_delete"),
    path('lote/<int:pk>/update/', LoteUpdateView.as_view(), name="lote_update"),
    path('lote/add', LoteCreateView.as_view(), name="lote_create"),
    path("lote/",  LoteListView.as_view(), name="lote_list"),
    path('plan-actividad-zafra/<int:pk>/update/', PlanActividadZafraUpdateView.as_view(), name="plan_actividad_zafra_update"),
    path('plan-actividad-zafra/add', PlanActividadZafraCreateView.as_view(), name="plan_actividad_zafra_create"),
    path("plan-actividad-zafra/",  PlanActividadZafraListView.as_view(), name="plan_actividad_zafra_list"),
]