from django.contrib import admin
from .models import Product, ProductVariant, ProductImage


# 🔹 Product Images Inline
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


# 🔹 Product Variants Inline
class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "is_featured",
        "is_active",
        "created_at"
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
        "created_at"
    )

    search_fields = ("name", "description")

    prepopulated_fields = {"slug": ("name",)}

    inlines = [ProductImageInline, ProductVariantInline]

    ordering = ("-created_at",)


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "size",
        "weight",
        "price",
        "stock",
        "is_default"
    )

    list_filter = ("product",)

    search_fields = ("product__name", "size")