from django.urls import path
from .views import update_car_location

app_name = "executive_cars"

urlpatterns = [
    path('', update_car_location, name="update_car_location"),
]