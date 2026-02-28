from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import ProductVariant
from .models import Cart, CartItem
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required
def add_to_cart(request, variant_id):

    variant = get_object_or_404(ProductVariant, id=variant_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        variant=variant
    )

    if not created:
        item.quantity += 1
        item.save()

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({
            "cart_count": cart.items.count(),
            "cart_total": cart.total_price()
        })

    return redirect("cart")


@login_required
def cart_view(request):

    cart, created = Cart.objects.get_or_create(user=request.user)

    return render(request, "orders/cart.html", {
        "cart": cart
    })

@require_POST
def update_quantity(request, item_id):

    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    quantity = int(request.POST.get("quantity"))

    if quantity > 0:
        item.quantity = quantity
        item.save()

    return JsonResponse({
        "item_total": item.total_price,
        "cart_total": item.cart.total_price()
    })


@require_POST
def remove_item(request, item_id):

    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart = item.cart
    item.delete()

    return JsonResponse({
        "cart_total": cart.total_price(),
        "cart_count": cart.items.count()
    })