from django.urls import path
from .views import add_to_executive_cars, remove_from_executive_cars

app_name = "executive_cars"

urlpatterns = [
    path('add_to_executive_cars/', add_to_executive_cars, name="add_to_executive_cars"),
    path('remove_from_executive_cars/', remove_from_executive_cars, name="remove_from_executive_cars"),
]