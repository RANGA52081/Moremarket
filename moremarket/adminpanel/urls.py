from django.urls import path
from . import views

urlpatterns = [

    # 📊 Control Center Dashboard
    path("", views.admin_dashboard, name="admin_dashboard"),
    path("login/", views.admin_login, name="login"),
    path("logout/", views.admin_logout, name="logout"),


    # 🎨 Banner Studio
    path("studio/banners/", views.banner_list, name="studio_banner_list"),
    path("studio/banners/create/", views.banner_create, name="studio_banner_create"),
    path("studio/banners/update/<int:pk>/", views.banner_edit, name="studio_banner_update"),
    path("studio/banners/toggle/<int:pk>/", views.banner_toggle, name="studio_banner_toggle"),
    path("studio/banners/archive/<int:pk>/", views.banner_archive, name="studio_banner_archive"),

    # 🔐 Security Center
    path("security/otps/", views.otp_list, name="security_otp_list"),
]