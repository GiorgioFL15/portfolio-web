from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('principal.urls')),
    path('admin/', admin.site.urls),
]
