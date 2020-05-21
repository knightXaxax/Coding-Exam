from django.shortcuts import render
from django.http import JsonResponse
from .models import ExecutiveCarsInformation


def add_to_executive_cars(request):
    if request.method == "POST":
        if request.POST['data']:
            data = request.POST['data'].split("-")
            new_executive_car = ExecutiveCarsInformation(name=data[0], color=data[1])
            new_executive_car.save(using="executive_cars")

            return JsonResponse({'msg' : 'okay'}, safe=True)


def remove_from_executive_cars(request):
    if request.method == "POST":
        if request.POST['data']:
            data = request.POST['data'].split("-")
            existing_executive_car = ExecutiveCarsInformation.objects.using('executive_cars').get(name=data[0])
            existing_executive_car.delete()
            return JsonResponse({'msg' : 'okay'}, safe=True)