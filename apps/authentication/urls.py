# -*- encoding: utf-8 -*-
from apps.authentication import views
from django.contrib.auth.views import LogoutView
from django.urls import include, path

urlpatterns = [
    path("accounts/users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user_delete"),
    path("accounts/users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user_update"),
    path("accounts/users/add", views.UserCreateView.as_view(), name="user_add"),
    path("accounts/users/", views.UserListView.as_view(), name="user_list"),
    path('accounts/login/', views.login_view, name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
]
