from django.urls import path, include
from .views import homepage, car_info, add_to_ordinary_cars, remove_from_ordinary_cars

app_name = "details"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('car_info/', car_info, name="car_info"),
    path('add_to_ordinary_cars/', add_to_ordinary_cars, name="add_to_ordinary_cars"),
    path('remove_from_ordinary_cars/', remove_from_ordinary_cars, name="remove_from_ordinary_cars"),
]