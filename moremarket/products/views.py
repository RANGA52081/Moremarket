from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
import json
from .models import Wishlist, Product
from django.contrib.auth.decorators import login_required

# 🔹 All Products Page
def product_list(request):
    category = request.GET.get("category")

    if category:
        products = Product.objects.filter(category=category, is_active=True)
    else:
        products = Product.objects.filter(is_active=True)

    return render(request, "products/product_list.html", {
        "products": products
    })


# 🔹 Product Detail Page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)

    variants = product.variants.all()

    default_variant = variants.filter(is_default=True).first()
    if not default_variant and variants.exists():
        default_variant = variants.first()

    # ✅ Collect image URLs safely
    image_urls = [img.image.url for img in product.images.all()]

    return render(request, "products/product_detail.html", {
        "product": product,
        "variants": variants,
        "default_variant": default_variant,
        "image_urls": json.dumps(image_urls)  # JSON format
    })

@login_required
def toggle_wishlist(request, pk):
    product = get_object_or_404(Product, pk=pk)

    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        wishlist_item.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related("product")

    return render(request, "products/wishlist.html", {
        "wishlist_items": wishlist_items
    })