from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q, Sum, Count
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from customer.models import Banner, UserOTP
from products.models import Product
from orders.models import Order
from .forms import BannerForm, ProductForm


# 🔐 Only staff users allowed
def admin_required(user):
    return user.is_staff


# ==============================
# ADMIN LOGIN
# ==============================

def admin_login(request):

    if request.user.is_authenticated and request.user.is_staff:
        return redirect("adminpanel:dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("adminpanel:dashboard")
        else:
            messages.error(request, "Invalid Admin Credentials")

    return render(request, "adminpanel/auth/login.html")


# ==============================
# ADMIN LOGOUT
# ==============================

def admin_logout(request):
    logout(request)
    return redirect("adminpanel:login")

from products.models import Product, ProductVariant
from django.db.models import Sum

@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def admin_dashboard(request):

    today = now().date()

    # 💰 Revenue
    total_revenue = Order.objects.aggregate(
        total=Sum("total_amount")
    )["total"] or 0

    today_revenue = Order.objects.filter(
        created_at__date=today
    ).aggregate(total=Sum("total_amount"))["total"] or 0

    # 📦 Orders
    total_orders = Order.objects.count()
    today_orders = Order.objects.filter(
        created_at__date=today
    ).count()

    # 🛍 Products & Users
    total_products = Product.objects.count()
    total_users = User.objects.count()

    # 🚨 LOW STOCK (Correct Way)


    low_stock_products = Product.objects.filter(
        variants__stock__lt=5
    ).distinct()

    top_product = Product.objects.annotate(
        total_sold=Sum("variants__orderitem__quantity")
    ).order_by("-total_sold").first()

    context = {
        "total_revenue": total_revenue,
        "today_revenue": today_revenue,
        "total_orders": total_orders,
        "today_orders": today_orders,
        "total_products": total_products,
        "total_users": total_users,
        "low_stock_products": low_stock_products,
        "top_product": top_product,
    }

    return render(request, "adminpanel/dashboard.html", context)

from customer.models import Banner
from .forms import BannerForm
from django.core.paginator import Paginator
from django.db.models import Q


@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def banner_list(request):

    search = request.GET.get("search", "")

    banners = Banner.objects.all().order_by("-created_at")

    if search:
        banners = banners.filter(
            Q(title__icontains=search) |
            Q(subtitle__icontains=search)
        )

    paginator = Paginator(banners, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "adminpanel/banner_list.html", {
        "page_obj": page_obj,
        "search": search
    })
from django.core.paginator import Paginator
from django.db.models import Q
from customer.models import Banner
from .forms import BannerForm


@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def banner_list(request):

    search = request.GET.get("search", "")
    banners = Banner.objects.all().order_by("-created_at")

    if search:
        banners = banners.filter(
            Q(title__icontains=search) |
            Q(subtitle__icontains=search)
        )

    paginator = Paginator(banners, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "adminpanel/banner_list.html", {
        "page_obj": page_obj,
        "search": search
    })


@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def banner_create(request):

    form = BannerForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("adminpanel:studio_banner_list")

    return render(request, "adminpanel/banner_form.html", {"form": form})


@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def banner_edit(request, pk):

    banner = get_object_or_404(Banner, pk=pk)
    form = BannerForm(request.POST or None, request.FILES or None, instance=banner)

    if form.is_valid():
        form.save()
        return redirect("adminpanel:studio_banner_list")

    return render(request, "adminpanel/banner_form.html", {"form": form})


@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def banner_toggle(request, pk):

    banner = get_object_or_404(Banner, pk=pk)
    banner.is_active = not banner.is_active
    banner.save()

    return redirect("adminpanel:studio_banner_list")


@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def banner_archive(request, pk):

    banner = get_object_or_404(Banner, pk=pk)
    banner.is_active = False
    banner.save()

    return redirect("adminpanel:studio_banner_list")

@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def admin_products(request):

    search = request.GET.get("search", "")

    products = Product.objects.all().order_by("-created_at")

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    paginator = Paginator(products, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "adminpanel/products.html", {
        "page_obj": page_obj,
        "search": search
    })
@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def product_create(request):

    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("adminpanel:products")

    return render(request, "adminpanel/product_form.html", {"form": form}) 

@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def product_edit(request, pk):

    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect("adminpanel:products")

    return render(request, "adminpanel/product_form.html", {"form": form})

@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def product_delete(request, pk):

    product = get_object_or_404(Product, pk=pk)
    product.delete()

    return redirect("adminpanel:products")