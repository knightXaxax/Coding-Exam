from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import CarsInformation
from operator import itemgetter
from .forms import EditForm
from django.urls import reverse


alpha_origin = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' ,'K','L', 'M',
        'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
]

alpha = []

def homepage(request):
    filtered = False
    cars = sorting_cars(CarsInformation.objects.all())
    car_names = sorted([car['name'] for car in cars])

    if request.method == "GET":
        return render(request, 'details/mainpages/homepage.html', {
            'title' : 'homepage',
            'cars' :  cars,
            'colors' : ['red', 'blue'],
        })
    
    elif request.method == "POST":
        car = {'color' : '', 'name' : ''}
        
        if request.POST['submit'] == 'blue-filter':
            cars = list(filter(lambda x: x['color'] == "blue", cars))
            filtered = True

        elif request.POST['submit'] == 'all-filter':
            cars = cars
            filtered = True

        elif request.POST['submit'] == 'red-filter':
            cars = list(filter(lambda x: x['color'] == "red", cars))
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
        })


def car_info(request):
    if request.method == "POST":
        car = CarsInformation.objects.get(id=request.POST['car_id'])

        if request.POST['submit'] == "update":
            car.color = request.POST['car_color']
            car.save()

        elif request.POST['submit'] == "delete":
            car.delete()

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