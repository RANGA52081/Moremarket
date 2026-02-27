

# Register your models here.
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

admin.site.site_header = "MoreMarket Admin"

def dashboard_link():
    return format_html(
        '<a href="/adminpanel/">Open Custom Admin Panel</a>'
    )

admin.site.index_title = "Dashboard"