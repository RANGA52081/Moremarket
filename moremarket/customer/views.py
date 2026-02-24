from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Banner
import random
from django.core.mail import send_mail
from django.conf import settings
from .models import UserOTP
from django.utils import timezone
from datetime import timedelta

# ========================
# HOME PAGE
# ========================
def customer_home(request):
    banners = Banner.objects.filter(is_active=True)

    return render(request, 'customer/customer.html', {
        'banners': banners
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

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        contact = request.POST.get("contact", "").strip()

        # -------------------------
        # Basic Validation
        # -------------------------
        if not username or not password or not contact:
            messages.error(request, "All fields are required")
            return redirect("register")

        # -------------------------
        # Detect Email or Phone
        # -------------------------
        if "@" in contact and "." in contact:
            email = contact
            phone = None
        elif contact.isdigit() and len(contact) == 10:
            email = None
            phone = contact
        else:
            messages.error(request, "Enter valid email or mobile number")
            return redirect("register")

        # -------------------------
        # Check Existing User
        # -------------------------
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if email and User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        # -------------------------
        # Create User (Inactive Until OTP Verified)
        # -------------------------
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active=False
        )

        # -------------------------
        # Generate OTP
        # -------------------------
        otp_code = str(random.randint(100000, 999999))

        UserOTP.objects.create(user=user, otp=otp_code)

        # -------------------------
        # Send Email OTP
        # -------------------------
        if email:
            send_mail(
                "MoreMarket OTP Verification",
                f"Your OTP is {otp_code}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

        # -------------------------
        # (Future) Send SMS OTP
        # -------------------------
        if phone:
            print("Send SMS OTP:", otp_code)
            # Integrate SMS API here later

        # Store user in session for verification
        request.session["otp_user"] = user.id

        return redirect("verify_otp")

    return render(request, "auth/register.html")


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
# ========================
# VERIFY OTP
# ========================

def verify_otp_view(request):

    user_id = request.session.get("otp_user")

    if not user_id:
        return redirect("register")

    user = User.objects.get(id=user_id)
    otp_record = UserOTP.objects.filter(user=user).last()

    if not otp_record:
        return redirect("register")

    # Auto delete expired OTP + user
    if otp_record.is_expired():
        user.delete()
        otp_record.delete()
        messages.error(request, "OTP expired. Please register again.")
        return redirect("register")

    if request.method == "POST":

        entered_otp = "".join([
        request.POST.get(f"otp{i}", "").strip()
        for i in range(1, 7)
        ])

        if not otp_record.can_retry():
            user.delete()
            otp_record.delete()
            messages.error(request, "Too many attempts. Please register again.")
            return redirect("register")

        if otp_record.otp == entered_otp:
            login(request, user)
            otp_record.delete()
            del request.session["otp_user"]
            return redirect("customer_home")

        else:
            otp_record.attempts += 1
            otp_record.save()
            messages.error(request, f"Invalid OTP ({otp_record.attempts}/3)")

    return render(request, "auth/verify_otp.html")
def resend_otp_view(request):

    user_id = request.session.get("otp_user")
    if not user_id:
        return redirect("register")

    user = User.objects.get(id=user_id)

    otp_code = str(random.randint(100000, 999999))

    UserOTP.objects.create(user=user, otp=otp_code)

    # Send Email
    if user.email:
        send_mail(
            "MoreMarket OTP",
            f"Your new OTP is {otp_code}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

    return JsonResponse({"status": "sent"})