from django.db.models import Sum, Count
from django.utils.timezone import now
from orders.models import Order
from products.models import Product
from django.contrib.auth.models import User

def dashboard_metrics():

    today = now().date()

    total_revenue = Order.objects.aggregate(
        total=Sum("total_amount")
    )["total"] or 0

    today_revenue = Order.objects.filter(
        created_at__date=today
    ).aggregate(total=Sum("total_amount"))["total"] or 0

    total_orders = Order.objects.count()
    today_orders = Order.objects.filter(created_at__date=today).count()

    total_products = Product.objects.count()
    total_users = User.objects.count()

    low_stock = Product.objects.filter(stock__lt=5)

    top_product = Product.objects.annotate(
        sold=Count("orderitem")
    ).order_by("-sold").first()

    return {
        "total_revenue": total_revenue,
        "today_revenue": today_revenue,
        "total_orders": total_orders,
        "today_orders": today_orders,
        "total_products": total_products,
        "total_users": total_users,
        "low_stock": low_stock,
        "top_product": top_product,
    }