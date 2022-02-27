from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('api.urls')),  # saadab api urls faili vaatama
    path('admin/', admin.site.urls),
]
