from django.contrib import admin
from .models import Banner, UserOTP, BannerImage


class BannerImageInline(admin.TabularInline):
    model = BannerImage
    extra = 1


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [BannerImageInline]

@admin.register(UserOTP)
class UserOTPAdmin(admin.ModelAdmin):
    list_display = ("user", "otp", "created_at")