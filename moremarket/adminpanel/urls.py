from django.urls import path
from . import views

app_name = "adminpanel"   # 🔥 VERY IMPORTANT

urlpatterns = [

    # 🔐 Authentication
    path("login/", views.admin_login, name="login"),
    path("logout/", views.admin_logout, name="logout"),

    # 📊 Dashboard
   # path("signup/", views.admin_signup, name="signup"),
   path("", views.admin_dashboard, name="dashboard"),
    path("products/", views.admin_products, name="products"),
    path("orders/", views.admin_orders, name="orders"),
    path("customers/", views.admin_customers, name="customers"),
    path("analytics/", views.admin_analytics, name="analytics"),

    # 🎨 Banner Studio
    path("studio/banners/", views.banner_list, name="studio_banner_list"),
    path("studio/banners/create/", views.banner_create, name="studio_banner_create"),
    path("studio/banners/update/<int:pk>/", views.banner_edit, name="studio_banner_update"),
    path("studio/banners/toggle/<int:pk>/", views.banner_toggle, name="studio_banner_toggle"),
    path("studio/banners/archive/<int:pk>/", views.banner_archive, name="studio_banner_archive"),

    
]