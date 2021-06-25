from requests import api
from main.models import City
from django import http
from django.shortcuts import redirect, render
import requests
from .forms import CityForm

API_KEY = '2c3bf5a1f57d4341d69a551ba5d562bd'
URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY

def index(request):
    form = CityForm()
    allCitiesInfo = []
    cities = City.objects.all()
    for city in cities:
        dataCurrentCity = requests.get(URL.format(city.name)).json()
        city = {
            'name': city.name,
            'temp': dataCurrentCity['main']['temp'],
            'icon': dataCurrentCity['weather'][0]['icon']
        }
        allCitiesInfo.append(city)

    if request.method == "POST":
        dataCurrentCity = requests.get(URL.format(request.POST.get('name'))).json()
        if dataCurrentCity['cod'] == '404':
            error = 'The city doesn\'t exist'
            return render(request, 'index.html', {'form': CityForm(), 'cities': allCitiesInfo, 'error': error})
        form = CityForm(request.POST)
        form.save()
        newCity = {
            'name': dataCurrentCity['name'],
            'temp': dataCurrentCity['main']['temp'],
            'icon': dataCurrentCity['weather'][0]['icon']
        }
        allCitiesInfo.append(newCity)
        return render(request, 'index.html', {'form': CityForm(), 'cities': allCitiesInfo})

    return render(request, 'index.html', {'form': form, 'cities': allCitiesInfo})

def delete(request, name):
    obj = City.objects.filter(name=name)
    obj.delete()
    return redirect(index)