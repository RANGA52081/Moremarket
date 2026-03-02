from django.db import models
from django.contrib.auth.models import User
from products.models import ProductVariant


# 🔹 Address Model
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    area = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.city}"


# 🔹 Cart Model
# 🔹 Cart Model
class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def total_weight(self):
        return sum(item.total_weight() for item in self.items.all())

    def total_quantity(self):
        return sum(item.quantity for item in self.items.all())

    def __str__(self):
        return f"Cart - {self.user.username}"


# 🔹 Cart Item
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("cart", "variant")  # Prevent duplicate same variant

    def total_price(self):
        return self.quantity * self.variant.price

    def total_weight(self):
        return self.quantity * self.variant.weight

    def __str__(self):
        return f"{self.variant.product.name} ({self.variant.size})"


# 🔹 Order Model
class Order(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_weight = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


# 🔹 Order Items
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.variant.product.name} - {self.quantity}"
class Enquiry(models.Model):

    STATUS_CHOICES = (
        ("Address Pending", "Address Pending"),
        ("Waiting Approval", "Waiting Approval"),
        ("Payment Pending", "Payment Pending"),
        ("Partially Paid", "Partially Paid"),
        ("Fully Paid", "Fully Paid"),
        ("Completed", "Completed"),
    )

    PAYMENT_MODE = (
        ("FULL", "Full Payment"),
        ("PARTIAL", "50% Advance"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE, null=True, blank=True)

    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    advance_enabled = models.BooleanField(default=False)
    final_enabled = models.BooleanField(default=False)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Address Pending")

    created_at = models.DateTimeField(auto_now_add=True)

    def remaining_amount(self):
        return self.total_amount - self.amount_paid

    def __str__(self):
        return f"Enquiry #{self.id} - {self.user.username}"