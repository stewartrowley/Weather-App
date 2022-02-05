from unicodedata import name
import requests
from django.shortcuts import render
from .forms import CityForm
from .models import City

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=483394b5f70d404d21682ecd4208e8a0'
    
    # city_list = []
    # citie = City.objects.all()
    # for n in citie:
    #     city_list.append(n)

    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        

    form = CityForm()

    cities = City.objects.all()

    weather = []

    for i in cities:

    # for city in cities:

        r = requests.get(url.format(i.name)).json()

        city_weather = {
            'city' : i.name,
            'temperature' : r['main']['temp'],
            'windspeed' : r['wind']['speed'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }

        weather.append(city_weather)

    context = {'weather' : weather, 'form' : form}

    return render(request, 'index.html', context)

def weather(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q=Rexburg&units=imperial&appid=483394b5f70d404d21682ecd4208e8a0'
    name = 'Rexburg'
    r = requests.get(url.format(name)).json()

    city_weathered = {
        'city' : name,
        'temperature' : r['main']['temp'],
        'humidity' : r['main']['humidity'],
        'temp_min' : r['main']['temp_min'],
        'temp_max' : r['main']['temp_max'],
        'windspeed' : r['wind']['speed'],
        'windgust' : r ['wind']['deg'],
        'sunrise' : r['sys']['sunrise'],
        'sunset' : r['sys']['sunset'],
        'base' : r['base'],
        'main' : r['weather'][0]['main'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon']
    }

    context = {'city_weathered' : city_weathered}

    return render(request, 'weather.html', context)