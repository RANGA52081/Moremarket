from django.shortcuts import render
from .models import Banner

def customer_home(request):
    return render(request, 'customer/customer.html')
def customer_home(request):
    banners = Banner.objects.filter(is_active=True)
    return render(request, 'customer/customer.html', {
        'banners': banners
    })