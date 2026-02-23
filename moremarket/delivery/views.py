from django.shortcuts import render, redirect

def delivery_dashboard(request):
    orders = [
        {"id": 1, "customer": "Ravi", "status": "Out for Delivery"},
        {"id": 2, "customer": "Arun", "status": "Pending"},
    ]
    return render(request, 'delivery/delivery.html', {"orders": orders})


def update_delivery_status(request, order_id):
    # Later connect to database
    return redirect('delivery_dashboard')