from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import CarsInformation
from operator import itemgetter
from .forms import EditForm
from django.urls import reverse
import threading
from executive_cars.models import ExecutiveCarsInformation


alpha_origin = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' ,'K','L', 'M',
        'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
]

alpha = []

def homepage(request):
    filtered = False
    cars = sorting_cars(CarsInformation.objects.all())
    executive_cars = sorting_cars(ExecutiveCarsInformation.objects.using('executive_cars').all())
    car_to_be_sorted = []
    for car in cars:
        car_to_be_sorted.append(car)

    for executive_car in executive_cars:
        car_to_be_sorted.append(executive_car)

    car_names = sorted([car['name'] for car in car_to_be_sorted])

    if request.method == "GET":
        print(car_names)
        return render(request, 'details/mainpages/homepage.html', {
            'title' : 'homepage',
            'cars' :  cars,
            'colors' : ['red', 'blue'],
            'executive_cars' : executive_cars,
        })
    
    elif request.method == "POST":
        car = {'color' : '', 'name' : ''}
        
        if request.POST['submit'] == 'blue-filter':
            cars = list(filter(lambda x: x['color'] == "blue", cars))
            executive_cars = list(filter(lambda x: x['color'] == "blue", executive_cars))
            filtered = True

        elif request.POST['submit'] == 'all-filter':
            cars = cars
            executive_cars = executive_cars
            filtered = True

        elif request.POST['submit'] == 'red-filter':
            cars = list(filter(lambda x: x['color'] == "red", cars))
            executive_cars = list(filter(lambda x: x['color'] == "red", executive_cars))
            filtered = True

        elif request.POST['submit'] == "add-blue-car":
            thousand_name_generator(car, car_names)
            car['color'] = "blue"
            change_color(car)

        elif request.POST['submit'] == "add-red-car":
            thousand_name_generator(car, car_names)
            car['color'] = "red"
            change_color(car)
        
        return render(request, 'details/mainpages/homepage.html', {
            'title' : 'homepage',
            'cars' : sorting_cars(CarsInformation.objects.all()) if not filtered == True else cars,
            'colors' : ['red', 'blue'],
            'executive_cars' : sorting_cars(ExecutiveCarsInformation.objects.using('executive_cars').all()) if not filtered == True else sorting_cars,
        })


def car_info(request):
    if request.method == "POST":
        car = ""
        executive_car = ""
        try:
            car = CarsInformation.objects.get(id=request.POST['car_id'])
        except Exception as e:
            try:
                executive_car = ExecutiveCarsInformation.objects.using('executive_cars').get(id=request.POST['car_id'])
            except Exception as e:
                car = CarsInformation.objects.get(id=request.POST['car_id'])

        if request.POST['submit'] == "update":
            if not car == "":
                car.color = request.POST['car_color']
                car.save()

            elif not executive_car == "":
                executive_car.color = request.POST['car_color']
                executive_car.save()

        elif request.POST['submit'] == "delete":
            if not car == "":
                car.delete()

            elif not executive_car == "":
                executive_car.delete()

        return redirect(reverse('details:homepage'))


def change_color(car):
    car = CarsInformation(name=car['name'], color=car['color'])
    car.save()


def sorting_cars(car_items):
    cars = [{
        'id' : car.id,
        'name' : car.name,
        'color' : car.color,
    } for car in car_items]
    cars.sort(key=itemgetter('name'))
    return cars


def thousand_name_generator(car, car_names):
    for letter in alpha_origin:
        alpha.append(letter)

    for iterator in range(1,len(alpha_origin)**4):
        for letter in alpha_origin:
            alpha.append(letter+str(iterator)) 

    for letter in alpha:
        if not str(letter) in car_names:
            car['name'] = letter
            break


def add_to_ordinary_cars(request):
    if request.method == "POST":
        if request.POST['data']:
            data = request.POST['data'].split("-")
            new_ordinary_car = CarsInformation(name=data[0], color=data[1])
            new_ordinary_car.save()

            return JsonResponse({'msg' : 'okay'}, safe=True)


def remove_from_ordinary_cars(request):
    if request.method == "POST":
        if request.POST['data']:
            data = request.POST['data'].split("-")
            existing_ordinary_car = CarsInformation.objects.get(name=data[0])
            existing_ordinary_car.delete()
            return JsonResponse({'msg' : 'okay'}, safe=True)