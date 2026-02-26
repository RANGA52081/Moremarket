from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Banner, UserOTP
from products.models import Product
import random
from django.core.mail import send_mail
from django.conf import settings
from .models import UserOTP, Address
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# ========================
# HOME PAGE
# ========================
def customer_home(request):
    banners = Banner.objects.filter(is_active=True)

    category = request.GET.get("category")

    if category:
        products = Product.objects.filter(category=category, is_active=True)
    else:
        products = Product.objects.filter(is_active=True)

    return render(request, 'customer/customer.html', {
        'banners': banners,
        'products': products,
        'active_category': category
    })
# ========================
# CART PAGE
# ========================
def cart_view(request):
    return render(request, "customer/cart.html")

# ========================
# SAVE LOCATION
# ========================
def save_location(request):
    if request.method == "POST":
        request.session['selected_location'] = request.POST.get("location")
        return JsonResponse({"status": "success"})


# ========================
# REGISTER
# ========================


def register_view(request):

    show_otp = False

    if request.method == "POST":

        form_type = request.POST.get("form_type")

        # ================= REGISTER =================
        if form_type == "register":

            username = request.POST.get("username")
            contact = request.POST.get("contact")
            password = request.POST.get("password")

            # 🔹 Check existing active username
            if User.objects.filter(username=username, is_active=True).exists():
                messages.error(request, "Username already exists")
                return render(request, "auth/register.html", {"show_otp": False})

            # 🔹 Check existing active email
            if User.objects.filter(email=contact, is_active=True).exists():
                messages.error(request, "Email already registered")
                return render(request, "auth/register.html", {"show_otp": False})

            # 🔹 If inactive user exists (from previous failed OTP), delete it
            existing_user = User.objects.filter(username=username, is_active=False).first()
            if existing_user:
                existing_user.delete()

            # 🔹 Create new inactive user
            user = User.objects.create_user(
                username=username,
                email=contact,
                password=password,
                is_active=False
            )

            # 🔹 Generate OTP
            otp_code = str(random.randint(100000, 999999))

            # Delete old OTPs for this user
            UserOTP.objects.filter(user=user).delete()

            # Save new OTP
            UserOTP.objects.create(user=user, otp=otp_code)

            # Store user id in session
            request.session["otp_user"] = user.id

            # 🔹 Send Email
            send_mail(
                "MoreMarket OTP Verification",
                f"Your OTP is {otp_code}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            show_otp = True

        # ================= VERIFY OTP =================
        elif form_type == "otp":

            user_id = request.session.get("otp_user")

            if not user_id:
                messages.error(request, "Session expired. Please register again.")
                return redirect("register")

            user = User.objects.get(id=user_id)
            otp_record = UserOTP.objects.filter(user=user).last()

            if not otp_record:
                messages.error(request, "OTP not found. Please register again.")
                return redirect("register")

            entered_otp = "".join([
                request.POST.get(f"otp{i}", "").strip()
                for i in range(1, 7)
            ])

            if entered_otp == otp_record.otp:

                # Activate user
                user.is_active = True
                user.save()

                # Cleanup
                otp_record.delete()
                del request.session["otp_user"]

                login(request, user)
                return redirect("customer_home")

            else:
                messages.error(request, "Invalid OTP")
                show_otp = True

    return render(request, "auth/register.html", {"show_otp": show_otp})

# ========================
# LOGIN
# ========================
def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("customer_home")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "auth/login.html")


# ========================
# LOGOUT
# ========================
def logout_view(request):
    logout(request)
    return redirect("customer_home")



@login_required
def profile_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    addresses = Address.objects.filter(user=request.user)

    return render(request, "customer/profile.html", {
        "orders": orders,
        "addresses": addresses
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully")
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'customer/change_password.html', {'form': form})
@login_required
def add_address(request):
    if request.method == "POST":
        Address.objects.create(
            user=request.user,
            full_name=request.POST.get("full_name"),
            phone=request.POST.get("phone"),
            address_line=request.POST.get("address"),
            city=request.POST.get("city"),
            state=request.POST.get("state"),
            pincode=request.POST.get("pincode"),
        )
        return redirect("profile")
@login_required
def update_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.phone = request.POST.get("phone")
        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES.get("profile_image")
        profile.save()
        return redirect("profile")