from django.shortcuts import render
from django.db.models import Q
from .models import Resto

def restaurant_list(request):
    resto_name = request.GET.get('resto', '')
    area = request.GET.get('area', '')
    tags = request.GET.get('tags', '')
    address = request.GET.get('address', '')
    
    restaurants = Resto.objects.all()

    if resto_name:
        restaurants = restaurants.filter(name__icontains=resto_name)
    if area:
        restaurants = restaurants.filter(area__icontains=area)
    if tags:
        restaurants = restaurants.filter(restotag__tag__icontains=tags).distinct()
    if address:
        restaurants = restaurants.filter(address__icontains=address)

    context = {
        'restaurants': restaurants,
        'filters': {
            'resto': resto_name,
            'area': area,
            'tags': tags,
            'address': address
        }
    }
    return render(request, 'core/restaurant_list.html', context)
