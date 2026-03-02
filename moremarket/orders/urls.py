from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("cart/", views.cart_view, name="cart_view"),
    path("add-to-cart/<int:variant_id>/", views.add_to_cart, name="add_to_cart"),
    path("update-quantity/<int:item_id>/", views.update_quantity, name="update_quantity"),
    path("remove-item/<int:item_id>/", views.remove_item, name="remove_item"),
    path("enquiry/", views.enquiry_start, name="enquiry_start"),
    path("cart-to-enquiry/", views.cart_to_enquiry, name="cart_to_enquiry"),
    path("add-multiple-to-cart/", views.add_multiple_to_cart, name="add_multiple_to_cart"),
    path("enquiry/payment/<int:pk>/", views.enquiry_payment, name="enquiry_payment"),
]