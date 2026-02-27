from django.urls import path
from . import views

app_name = "adminpanel"

urlpatterns = [

    # 🔐 Authentication
    path("login/", views.admin_login, name="login"),
    path("logout/", views.admin_logout, name="logout"),

    # 📊 Dashboard
    path("", views.admin_dashboard, name="dashboard"),

    # 📦 Orders
    path("orders/", views.admin_orders, name="orders"),

    # 🛍 Products
    path("products/", views.admin_products, name="products"),
    path("products/create/", views.product_create, name="product_create"),
    path("products/edit/<int:pk>/", views.product_edit, name="product_edit"),
    path("products/delete/<int:pk>/", views.product_delete, name="product_delete"),

    # 🎨 Banner Studio
    path("studio/banners/", views.banner_list, name="studio_banner_list"),
    path("studio/banners/create/", views.banner_create, name="studio_banner_create"),
    path("studio/banners/update/<int:pk>/", views.banner_edit, name="studio_banner_update"),
    path("studio/banners/toggle/<int:pk>/", views.banner_toggle, name="studio_banner_toggle"),
    path("studio/banners/archive/<int:pk>/", views.banner_archive, name="studio_banner_archive"),
]