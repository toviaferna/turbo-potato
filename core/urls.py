# -*- encoding: utf-8 -*-

from django.urls import include, path  # add this

urlpatterns = [         # Django admin route
    path("", include("apps.authentication.urls")),
    path("reports/", include("apps.reports.urls")),
    path("sales/", include("apps.sales.urls")),
    path("farming/", include("apps.farming.urls")),
    path("inventory/", include("apps.inventory.urls")),
    path("finance/", include("apps.finance.urls")),
    path("supplies/", include("apps.supplies.urls")),
    path("", include("apps.home.urls")),
]
