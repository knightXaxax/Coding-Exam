from django.urls import path, include
from .views import homepage, car_info

app_name = "details"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('car_info/', car_info, name="car_info"),
    path('update_car_location/', include('executive_cars.urls')),
]