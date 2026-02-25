from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('MS', 'MS Scaffolding'),
        ('AL', 'Aluminium Scaffolding'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # ✅ ADD THIS
    created_at = models.DateTimeField(auto_now_add=True)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    size = models.CharField(max_length=20)   # 3m, 2.5m etc
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.size}m"