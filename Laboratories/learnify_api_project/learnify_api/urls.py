from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls), # No usaremos el admin
    path('api/', include('courses.urls')),
]