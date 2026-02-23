from django.shortcuts import render

def analytics_dashboard(request):
    context = {
        "daily_orders": 120,
        "total_sales": 56000,
        "pending_orders": 8,
    }
    return render(request, 'analytics/analytics.html', context)