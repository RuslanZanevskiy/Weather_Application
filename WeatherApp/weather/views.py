from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
	appid = 'be13ba75ec753a2414677215a39914eb'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid




	if(request.method == 'POST'):
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()

	all_cities = []

	try:
		for city in cities:
			res = requests.get(url.format(city.name)).json()
			city_info = {
				'city': city.name,
				'temp': res['main']['temp'],
				'icon': res['weather'][0]['icon'],
			}
			all_cities.append(city_info)
	except Exception as e:
		pass
	context = {
		'all_info': all_cities, 'form': form
	}
	return render(request, 'weather/index.html', context)
