from django import forms
from django.forms import widgets
from django_filters import FilterSet
import django_filters

from django.contrib.auth.models import User


class UserFilter(FilterSet):
    date_joined = django_filters.DateRangeFilter(
        widget= forms.RadioSelect(),
        empty_label = "Todos"
    )
    class Meta:
        model = User
        fields = ["is_superuser","is_staff","is_active","date_joined"]

