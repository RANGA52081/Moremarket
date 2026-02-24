"""
URL configuration for moremarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from customer import views as customer_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('adminpanel/', include('adminpanel.urls')),
    path('analytics/', include('analytics.urls')),
    path('delivery/', include('delivery.urls')),
<<<<<<< HEAD
    path('control/', include('adminpanel.urls')),
=======
    path('login/', customer_views.login_view, name='login'),
    path('register/', customer_views.register_view, name='register'),
    path('logout/', customer_views.logout_view, name='logout'),
    
>>>>>>> 885a4ad1efac7fdc4e980fdefbf891307a433551
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)