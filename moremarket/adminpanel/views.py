from django.shortcuts import render, redirect, get_object_or_404
from customer.models import Banner, UserOTP
from .forms import BannerForm
from django.contrib.auth.decorators import login_required


@login_required
def banner_list(request):
    banners = Banner.objects.all().order_by("-created_at")
    return render(request, "adminpanel/banner_list.html", {"banners": banners})


@login_required
def banner_create(request):
    form = BannerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("admin_banner_list")
    return render(request, "adminpanel/banner_form.html", {"form": form})


@login_required
def banner_edit(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    form = BannerForm(request.POST or None, request.FILES or None, instance=banner)
    if form.is_valid():
        form.save()
        return redirect("admin_banner_list")
    return render(request, "adminpanel/banner_form.html", {"form": form})


@login_required
def banner_delete(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    banner.delete()
    return redirect("admin_banner_list")


@login_required
def otp_list(request):
    otps = UserOTP.objects.all().order_by("-created_at")
    return render(request, "adminpanel/otp_list.html", {"otps": otps})