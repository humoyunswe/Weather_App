from django.shortcuts import render

from django.http import HttpResponse

from requests import get
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse('<h1>Weather_App</h1>')


def weather_info(request,city):
    city_name = city
    url = get(f"https://goweather.herokuapp.com/weather/{city_name}").json()
    x = url

    xarorat = x['temperature']
    shamol = x['wind']
    xolat = x['description']
    sana = datetime.now().date()

    return render(request,'weather/index.html',context={'xarorat':xarorat,'shamol':shamol,'xolat':xolat,'sana':sana,'city':city})

