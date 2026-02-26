from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_home, name='customer_home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('save-location/', views.save_location, name='save_location'),
    path('cart/', views.cart_view, name='cart'),
    path("profile/", views.profile_view, name="profile"),
    ]