from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('apka/', include('appOnLinux.urls')),
    path('admin/', admin.site.urls),
]
