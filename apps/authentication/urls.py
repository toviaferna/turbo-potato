# -*- encoding: utf-8 -*-
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from apps.authentication import views

urlpatterns = [
    path("accounts/users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user_delete"),
    path("accounts/users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user_update"),
    path("accounts/users/add", views.UserCreateView.as_view(), name="user_add"),
    path("accounts/users/", views.UserListView.as_view(), name="user_list"),
    path('accounts/login/', views.login_view, name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('backup/', views.DatabaseBackupView.as_view(), name='database_backup'),
    path('backup/list', views.BackupListView.as_view(), name='database_backup_list'),
]
