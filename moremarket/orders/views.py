from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import ProductVariant
from .models import Cart, CartItem


@login_required
def add_to_cart(request, variant_id):
    variant = get_object_or_404(ProductVariant, id=variant_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        variant=variant
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("orders:cart_view")


@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, "orders/cart.html", {"cart": cart})