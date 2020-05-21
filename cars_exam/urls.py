from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('details.urls')),
    path('executive_cars/', include('executive_cars.urls')),
]
