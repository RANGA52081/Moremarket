from django.db import models
from django.utils.text import slugify


class Product(models.Model):

    CATEGORY_CHOICES = (
        ('MS', 'MS Scaffolding'),
        ('AL', 'Aluminium Scaffolding'),
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()

    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# 🔹 Multiple Images (for hover scroll)
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"Image of {self.product.name}"


# 🔹 Variants (Size / Weight / Price / Stock)
class ProductVariant(models.Model):

    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="variants"
    )

    size = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=6, decimal_places=2)

    # 🔥 NEW FIELDS
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.PositiveIntegerField(default=0)

    stock = models.PositiveIntegerField(default=0)
    is_default = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_default', 'size']

    # 🔥 AUTO CALCULATED PRICE
    @property
    def price(self):
        if self.discount_percent > 0:
            discount_amount = (
                self.original_price * self.discount_percent / 100
            )
            return round(self.original_price - discount_amount, 2)
        return self.original_price

    def __str__(self):
        return f"{self.product.name} - {self.size}"
    
class Wishlist(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wishlist"
    )

    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
