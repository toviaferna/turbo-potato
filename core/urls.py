# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.urls import include, path  # add this

urlpatterns = [         # Django admin route
    path("", include("apps.authentication.urls")),
    url(r'^docs/', include('apps.documentation.urls', namespace='documentation')),
    path("reports/", include("apps.reports.urls")), 
    path("sales/", include("apps.sales.urls")), 
    path("farming/", include("apps.farming.urls")),             # UI Kits Html files
    path("inventory/", include("apps.inventory.urls")),             # UI Kits Html files
    path("finance/", include("apps.finance.urls")),             # UI Kits Html files
    path("supplies/", include("apps.supplies.urls")),             # UI Kits Html files
    path("", include("apps.home.urls")),             # UI Kits Html files
]
