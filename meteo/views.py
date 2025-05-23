from datetime import datetime
import geocoder
import requests
from django.http import HttpResponse
from django.template import loader
from meteo.models import Worldcities


def temp_somewhere(request):
    random_city = Worldcities.objects.all().order_by('?').first()
    city = random_city.city
    location = [random_city.lat, random_city.lng]
    temp = get_temp(location)
    template = loader.get_template("index.html")
    context = {
        'city': city,
        'temp': temp,
    }
    return HttpResponse(template.render(context, request))

def temp_here(request):
    location = geocoder.ip('me').latlng
    temp = get_temp(location)
    template = loader.get_template("index.html")
    context = {
        'city': "Your Location",
        'temp': temp,
    }
    return HttpResponse(template.render(context, request))


def get_temp(location):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m&temperature_unit=fahrenheit"
    now = datetime.now()
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']['temperature_2m'][hour]
    return temp