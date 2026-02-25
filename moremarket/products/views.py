from django.shortcuts import render, get_object_or_404
from .models import Product


# 🔹 All Products Page
def product_list(request):
    category = request.GET.get("category")

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    return render(request, "products/product_list.html", {
        "products": products
    })


# 🔹 Product Detail Page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    variants = product.variants.all()

    return render(request, "products/product_detail.html", {
        "product": product,
        "variants": variants
    })