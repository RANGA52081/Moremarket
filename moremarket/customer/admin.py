from django.contrib import admin
from .models import Banner, Address, UserOTP





@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")


@admin.register(UserOTP)
class UserOTPAdmin(admin.ModelAdmin):
    list_display = ("user", "otp", "created_at")