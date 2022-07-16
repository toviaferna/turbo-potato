from apps.farming import views
from django.urls import path

urlpatterns = [
    path(
        "finca/<int:pk>/delete/", views.FincaDeleteView.as_view(), name="finca_delete"
    ),
    path(
        "finca/<int:pk>/update/", views.FincaUpdateView.as_view(), name="finca_update"
    ),
    path("finca/add", views.FincaCreateView.as_view(), name="finca_create"),
    path("finca/", views.FincaListView.as_view(), name="finca_list"),
    path(
        "calificacion-agricola/<int:pk>/delete/",
        views.CalificacionAgricolaDeleteView.as_view(),
        name="calificacion_agricola_delete",
    ),
    path(
        "calificacion-agricola/<int:pk>/update/",
        views.CalificacionAgricolaUpdateView.as_view(),
        name="calificacion_agricola_update",
    ),
    path(
        "calificacion-agricola/add",
        views.CalificacionAgricolaCreateView.as_view(),
        name="calificacion_agricola_create",
    ),
    path(
        "calificacion-agricola/",
        views.CalificacionAgricolaListView.as_view(),
        name="calificacion_agricola_list",
    ),
    path(
        "tipo-actividad-agricola/<int:pk>/delete/",
        views.TipoActividadAgricolaDeleteView.as_view(),
        name="tipo_actividad_agricola_delete",
    ),
    path(
        "tipo-actividad-agricola/<int:pk>/update/",
        views.TipoActividadAgricolaUpdateView.as_view(),
        name="tipo_actividad_agricola_update",
    ),
    path(
        "tipo-actividad-agricola/add",
        views.TipoActividadAgricolaCreateView.as_view(),
        name="tipo_actividad_agricola_create",
    ),
    path(
        "tipo-actividad-agricola/",
        views.TipoActividadAgricolaListView.as_view(),
        name="tipo_actividad_agricola_list",
    ),
    path(
        "tipo-maquinaria-agricola/<int:pk>/delete/",
        views.TipoMaquinariaAgricolaDeleteView.as_view(),
        name="tipo_maquinaria_agricola_delete",
    ),
    path(
        "tipo-maquinaria-agricola/<int:pk>/update/",
        views.TipoMaquinariaAgricolaUpdateView.as_view(),
        name="tipo_maquinaria_agricola_update",
    ),
    path(
        "tipo-maquinaria-agricola/add",
        views.TipoMaquinariaAgricolaCreateView.as_view(),
        name="tipo_maquinaria_agricola_create",
    ),
    path(
        "tipo-maquinaria-agricola/",
        views.TipoMaquinariaAgricolaListView.as_view(),
        name="tipo_maquinaria_agricola_list",
    ),
    path(
        "maquinaria-agricola/<int:pk>/delete/",
        views.MaquinariaAgricolaDeleteView.as_view(),
        name="maquinaria_agricola_delete",
    ),
    path(
        "maquinaria-agricola/<int:pk>/update/",
        views.MaquinariaAgricolaUpdateView.as_view(),
        name="maquinaria_agricola_update",
    ),
    path(
        "maquinaria-agricola/add",
        views.MaquinariaAgricolaCreateView.as_view(),
        name="maquinaria_agricola_create",
    ),
    path(
        "maquinaria-agricola/",
        views.MaquinariaAgricolaListView.as_view(),
        name="maquinaria_agricola_list",
    ),
    path(
        "zafra/<int:pk>/delete/", views.ZafraDeleteView.as_view(), name="zafra_delete"
    ),
    path(
        "zafra/<int:pk>/update/", views.ZafraUpdateView.as_view(), name="zafra_update"
    ),
    path("zafra/add", views.ZafraCreateView.as_view(), name="zafra_create"),
    path("zafra/", views.ZafraListView.as_view(), name="zafra_list"),
    path("lote/<int:pk>/delete/", views.LoteDeleteView.as_view(), name="lote_delete"),
    path("lote/<int:pk>/update/", views.LoteUpdateView.as_view(), name="lote_update"),
    path("lote/add", views.LoteCreateView.as_view(), name="lote_create"),
    path("lote/", views.LoteListView.as_view(), name="lote_list"),
    path(
        "plan-actividad-zafra/<int:pk>/update/",
        views.PlanActividadZafraUpdateView.as_view(),
        name="plan_actividad_zafra_update",
    ),
    path(
        "plan-actividad-zafra/add",
        views.PlanActividadZafraCreateView.as_view(),
        name="plan_actividad_zafra_create",
    ),
    path(
        "plan-actividad-zafra/",
        views.PlanActividadZafraListView.as_view(),
        name="plan_actividad_zafra_list",
    ),
    path(
        "contrato/<int:pk>/delete/",
        views.ContratoDeleteView.as_view(),
        name="contrato_delete",
    ),
    path("contrato/add", views.ContratoCreateView.as_view(), name="contrato_create"),
    path("contrato/", views.ContratoListView.as_view(), name="contrato_list"),
    path(
        "acopio/<int:pk>/delete/",
        views.AcopioAnnulledView.as_view(),
        name="acopio_delete",
    ),
    path(
        "acopio/<int:pk>/update/",
        views.AcopioUpdateView.as_view(),
        name="acopio_update",
    ),
    path("acopio/add", views.AcopioCreateView.as_view(), name="acopio_create"),
    path("acopio/", views.AcopioListView.as_view(), name="acopio_list"),
    path(
        "actividad-agricola/<int:pk>/delete/",
        views.ActividadAgricolaAnnulledView.as_view(),
        name="actividad_agricola_delete",
    ),
    path(
        "actividad-agricola/add",
        views.ActividadAgricolaCreateView.as_view(),
        name="actividad_agricola_create",
    ),
    path(
        "actividad-agricola/",
        views.ActividadAgricolaListView.as_view(),
        name="actividad_agricola_list",
    ),
    # path("actividad-agricola/<int:pk>/delete/", views.ActividadAgricolaAnnulledView.as_view(), name="actividad_agricola_delete"),
    # path("actividad-agricola/add", views.ActividadAgricolaCreateView.as_view(), name="actividad_agricola_create"),
    path(
        "liquidacion-agricola/",
        views.LiquidacionAgricolaListView.as_view(),
        name="liquidacion_agricola_list",
    ),
    path(
        "liquidacion-agricola/selection",
        views.LiquidacionAgricolaSelectionView.as_view(),
        name="liquidacion_agricola_selection",
    ),
    path(
        "liquidacion-agricola/add",
        views.LiquidacionAgricolaCreateView.as_view(),
        name="liquidacion_agricola_create",
    ),
    path(
        "cierre-zafra/<int:pk>/delete/",
        views.CierreZafraDeleteView.as_view(),
        name="cierre_zafra_delete",
    ),
    path(
        "cierre-zafra/add",
        views.CierreZafraCreateView.as_view(),
        name="cierre_zafra_create",
    ),
    path(
        "cierre-zafra/selection",
        views.CierreZafraSelectionView.as_view(),
        name="cierre_zafra_selection",
    ),
    path(
        "cierre-zafra/", views.CierreZafraListView.as_view(), name="cierre_zafra_list"
    ),
]
