from django.urls import path
from . import views

urlpatterns = [
    path("banners/", views.banner_list, name="admin_banner_list"),
    path("banners/add/", views.banner_create, name="admin_banner_create"),
    path("banners/edit/<int:pk>/", views.banner_edit, name="admin_banner_edit"),
    path("banners/delete/<int:pk>/", views.banner_delete, name="admin_banner_delete"),

    path("otp/", views.otp_list, name="admin_otp_list"),
]