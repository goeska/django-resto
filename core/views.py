from django.shortcuts import render
from .models import Resto

def restaurant_list(request):
    tag_query = request.GET.get('tag', '')
    
    if tag_query:
        # Filter restaurants that have a RestoTag matching the query (case-insensitive)
        restaurants = Resto.objects.filter(restotag__tag__icontains=tag_query).distinct()
    else:
        restaurants = Resto.objects.all()
        
    context = {
        'restaurants': restaurants,
        'tag_query': tag_query
    }
    return render(request, 'core/restaurant_list.html', context)
