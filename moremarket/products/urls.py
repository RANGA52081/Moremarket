from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path("wishlist/<int:pk>/", views.toggle_wishlist, name="toggle_wishlist"),  # 🔥 THIS
]