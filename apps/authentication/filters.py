import django_filters
from apps.authentication import models
from django import forms
from django_filters import FilterSet


class UserFilter(FilterSet):
    date_joined = django_filters.DateRangeFilter(
        widget= forms.RadioSelect(),
        empty_label = "Todos"
    )
    class Meta:
        model = models.User
        fields = ["is_active","date_joined"]

