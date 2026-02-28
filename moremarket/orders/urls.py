from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("cart/", views.cart_view, name="cart_view"),
    path("add-to-cart/<int:variant_id>/", views.add_to_cart, name="add_to_cart"),
    path("update-quantity/<int:item_id>/", views.update_quantity, name="update_quantity"),
    path("remove-item/<int:item_id>/", views.remove_item, name="remove_item"),
]