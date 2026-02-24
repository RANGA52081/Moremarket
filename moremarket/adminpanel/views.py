from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# =========================
# Signup View
# =========================
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            return redirect('login')
        else:
            return render(request, 'adminpanel/signup.html', {
                'error': 'Username already exists'
            })

    return render(request, 'adminpanel/signup.html')


# =========================
# Login View
# =========================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'adminpanel/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'adminpanel/login.html')


# =========================
# Logout View
# =========================
def logout_view(request):
    logout(request)
    return redirect('login')


# =========================
# Dashboard (Protected)
# =========================
@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'adminpanel/dashboard.html')