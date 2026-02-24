from django.urls import path
from . import views

app_name = "adminpanel"

urlpatterns = [
    path('auth/signup/', views.signup_view, name='signup'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('', views.admin_dashboard, name='dashboard'),  # Default admin home
]