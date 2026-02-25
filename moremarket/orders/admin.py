from django.contrib import admin

from moremarket.orders.models import Address

# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "city", "pincode")