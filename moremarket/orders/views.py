from pyexpat.errors import messages
from customer.models import Address
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import ProductVariant
from .models import Cart, CartItem, Enquiry
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

# ===============================
# ADD TO CART
# ===============================
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
            "cart_count": cart.total_quantity(),
            "cart_total": cart.total_price()
        })

    return redirect("cart")


# ===============================
# CART PAGE
# ===============================
@login_required
def cart_view(request):

    cart, created = Cart.objects.get_or_create(user=request.user)

    return render(request, "orders/cart.html", {
        "cart": cart
    })


def enquiry_payment(request, pk):
    enquiry = get_object_or_404(Enquiry, pk=pk)
    return render(request, "orders/enquiry_payment.html", {
        "enquiry": enquiry
    })
# ===============================
# UPDATE QUANTITY (AJAX)
# ===============================
@login_required
@require_POST
def update_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    quantity = int(request.POST.get("quantity", 1))

    if quantity > 0:
        item.quantity = quantity
        item.save()

    return JsonResponse({
        "item_total": item.total_price(),  # FIXED
        "cart_total": item.cart.total_price(),
        "cart_count": item.cart.total_quantity()
    })


# ===============================
# REMOVE ITEM (AJAX)
# ===============================
@login_required
@require_POST
def remove_item(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    cart = item.cart
    item.delete()

    return JsonResponse({
        "cart_total": cart.total_price(),
        "cart_count": cart.total_quantity()
    })
@login_required
def cart_to_enquiry(request):
    cart = Cart.objects.filter(user=request.user).first()

    if not cart or not cart.items.exists():
        return redirect("cart")

    # Later we will convert cart to enquiry
    return redirect("orders:enquiry_start")
@login_required
def add_multiple_to_cart(request):

    if request.method == "POST":

        data = json.loads(request.body)
        variants = data.get("variants", [])

        cart, created = Cart.objects.get_or_create(user=request.user)

        for item in variants:
            variant_id = item.get("id")
            quantity = int(item.get("quantity", 1))

            variant = get_object_or_404(ProductVariant, id=variant_id)

            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                variant=variant
            )

            if created:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity

            cart_item.save()

        return JsonResponse({"status": "success"})

    return JsonResponse({"error": "invalid request"})
@login_required
def enquiry_start(request):

    address = Address.objects.filter(user=request.user).first()

    if not address:
        return redirect("customer:add_address")   # ✅ changed here

    return redirect("orders:cart_to_enquiry")
    return redirect("orders:cart_to_enquiry")
@login_required
def cart_to_enquiry(request):

    cart = Cart.objects.filter(user=request.user).first()

    if not cart or not cart.items.exists():
        messages.error(request, "Please select a product before enquiry.")
        return redirect("customer_home")

    return render(request, "orders/enquiry.html", {
        "cart": cart
    })