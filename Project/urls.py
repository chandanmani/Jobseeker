"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# Import necessary modules
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT
from .views import Main,register,user_login,user_logout,send_custom_email

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main, name="Main"),  # Define a separate view for the root URL
    path('', include("Homes.urls")),
    path("Register/",register,name="register"),
    path("login/",user_login,name="login"),
    path("logout/",user_logout,name="logout"),
    path('SendEmail/',send_custom_email,name="send_email")
        
]

# Serve media files during development
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
