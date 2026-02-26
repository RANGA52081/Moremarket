from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q, Sum, Count
from django.utils.timezone import now
from django.contrib.auth.models import User

from customer.models import Banner, UserOTP
from products.models import Product
from orders.models import Order
from .forms import BannerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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


# ==============================
# ADMIN DASHBOARD
# ==============================

@login_required(login_url="adminpanel:login")
@user_passes_test(admin_required, login_url="adminpanel:login")
def admin_dashboard(request):
    return render(request, "adminpanel/dashboard.html")

# =====================================================
# 🔐 Role Check (Only Staff/Admin Allowed)
# =====================================================

def admin_required(user):
    return user.is_staff


# =====================================================
# 📊 DASHBOARD – MoreMarket Control Center
# =====================================================

@login_required
@user_passes_test(admin_required)
def admin_dashboard(request):

    today = now().date()

    # Revenue Metrics
    total_revenue = Order.objects.aggregate(
        total=Sum("total_amount")
    )["total"] or 0

    today_revenue = Order.objects.filter(
        created_at__date=today
    ).aggregate(total=Sum("total_amount"))["total"] or 0

    # Orders Metrics
    total_orders = Order.objects.count()
    today_orders = Order.objects.filter(
        created_at__date=today
    ).count()

    # Product & User Metrics
    total_products = Product.objects.count()
    total_users = User.objects.count()

    # Low Stock Alert
    low_stock_products = Product.objects.filter(stock__lt=5)

    # Top Selling Product
    top_product = Product.objects.annotate(
        total_sold=Count("orderitem")
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


# =====================================================
# 🎨 BANNER STUDIO
# =====================================================

@login_required
@user_passes_test(admin_required)
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


@login_required
@user_passes_test(admin_required)
def banner_create(request):

    form = BannerForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("studio_banner_list")

    return render(request, "adminpanel/banner_form.html", {"form": form})


@login_required
@user_passes_test(admin_required)
def banner_edit(request, pk):

    banner = get_object_or_404(Banner, pk=pk)

    form = BannerForm(request.POST or None, request.FILES or None, instance=banner)

    if form.is_valid():
        form.save()
        return redirect("studio_banner_list")

    return render(request, "adminpanel/banner_form.html", {"form": form})


@login_required
@user_passes_test(admin_required)
def banner_toggle(request, pk):

    banner = get_object_or_404(Banner, pk=pk)
    banner.is_active = not banner.is_active
    banner.save()

    return redirect("studio_banner_list")


@login_required
@user_passes_test(admin_required)
def banner_archive(request, pk):

    banner = get_object_or_404(Banner, pk=pk)
    banner.is_active = False
    banner.save()

    return redirect("studio_banner_list")


# =====================================================
# 🔐 OTP MONITORING (Security Center)
# =====================================================

@login_required
@user_passes_test(admin_required)
def otp_list(request):

    otps = UserOTP.objects.all().order_by("-created_at")

    paginator = Paginator(otps, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "adminpanel/otp_list.html", {
        "page_obj": page_obj
    })

from .models import AdminUser


# ==============================
# ADMIN SIGNUP
# ==============================

def admin_signup(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if AdminUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            admin = AdminUser(username=username, email=email)
            admin.set_password(password)
            admin.save()

            messages.success(request, "Admin account created. Please login.")
            return redirect("adminpanel:login")

    return render(request, "adminpanel/auth/signup.html")


# ==============================
# ADMIN LOGIN
# ==============================

def admin_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            admin = AdminUser.objects.get(username=username)

            if admin.check_password(password):
                request.session["admin_id"] = admin.id
                return redirect("adminpanel:dashboard")
            else:
                messages.error(request, "Invalid credentials.")

        except AdminUser.DoesNotExist:
            messages.error(request, "Admin not found.")

    return render(request, "adminpanel/auth/login.html")


# ==============================
# ADMIN LOGOUT
# ==============================

def admin_logout(request):
    request.session.flush()
    return redirect("adminpanel:login")


# ==============================
# DASHBOARD (Protected)
# ==============================

def admin_dashboard(request):

    if not request.session.get("admin_id"):
        return redirect("adminpanel:login")

    admin = AdminUser.objects.get(id=request.session["admin_id"])

    return render(request, "adminpanel/dashboard.html", {"admin": admin})