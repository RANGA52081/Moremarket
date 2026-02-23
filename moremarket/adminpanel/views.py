from django.shortcuts import render

def admin_home(request):
    return render(request, 'adminpanel/admin.html')