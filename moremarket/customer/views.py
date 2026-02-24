from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Banner


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
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect("customer_home")

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