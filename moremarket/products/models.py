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
        Product,
        on_delete=models.CASCADE,
        related_name="variants"
    )

    size = models.CharField(max_length=20)   # 3m, 2.5m
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    is_default = models.BooleanField(default=False)

    class Meta:
        ordering = ['size']

    def __str__(self):
        return f"{self.product.name} - {self.size}"
    

