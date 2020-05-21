from django.shortcuts import render
from django.http import JsonResponse


def update_car_location(request):
    if request.method == "POST":
        if request.POST['data']:
            return JsonResponse({'data' : request.POST['data']}, safe=True)