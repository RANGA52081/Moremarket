from django.shortcuts import render
from products.models import Product
from orders.models import Order
from django.contrib.auth.models import User

def admin_dashboard(request):
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_users = User.objects.count()
    total_revenue = sum(order.total_amount for order in Order.objects.all())

    context = {
        "total_products": total_products,
        "total_orders": total_orders,
        "total_users": total_users,
        "total_revenue": total_revenue
    }

    return render(request, "adminpanel/dashboard.html", context)