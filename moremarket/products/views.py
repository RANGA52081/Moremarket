from django.shortcuts import render, get_object_or_404
from .models import Product


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

    if not default_variant:
        default_variant = variants.first()

    if not default_variant:
        # No variants at all
        return render(request, "products/product_detail.html", {
            "product": product,
            "variants": [],
            "default_variant": None
        })

    return render(request, "products/product_detail.html", {
        "product": product,
        "variants": variants,
        "default_variant": default_variant
    })