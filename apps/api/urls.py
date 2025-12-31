"""
URL configuration for admin-user-api project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),  # Django built-in admin (optional, at different path)
    path('', include('main.tracker.urls')),  # Include tracker app URLs (includes /admin/ for custom portal)
]

