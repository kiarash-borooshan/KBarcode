from . import views
from django.urls import path

""" em = Earth Monitor """

app_name = 'account'

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("register_em/", views.register_em_user, name="register_em"),
    path("login/", views.login_user, name="login"),
    path("login_em/", views.login_em_user, name="login_em"),
    path("logout/", views.logout_user, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard_em/", views.dashboard_em, name="dashboard_em"),
    path("dashboard/edit_info/", views.edit_info, name="edit_info"),
    path("change_password/", views.edit_password, name="change_password"),
    path("delete_account/", views.delete_account, name="delete_account"),
]
