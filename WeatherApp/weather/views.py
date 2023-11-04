from django.shortcuts import render
from django.conf import settings
import requests

import os

from .models import City
from .forms import CityForm


APPID = settings.APPID


def index(request):
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + APPID

	if(request.method == 'POST'):
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()

	all_cities = []

	for city in cities:
		try:
			res = requests.get(url.format(city.name)).json()
			city_info = {
				'city': city.name,
				'temp': res['main']['temp'],
				'icon': res['weather'][0]['icon'],
			}
			all_cities.append(city_info)
		except Exception as e:
			print(city)
			print(e)

	context = {
		'all_info': all_cities, 'form': form
	}

	return render(request, 'weather/index.html', context)
