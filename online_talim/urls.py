from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('auth/', include('djoser.urls')),
    path('token/auth/', include('djoser.urls.authtoken')),
    path('api/courses/', include('courses.urls')),  
]
