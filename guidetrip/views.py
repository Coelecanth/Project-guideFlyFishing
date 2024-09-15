from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import trips

# Create your views here.
def all_trips(request):
    """ A view to return the all trips and show sorting and search result"""

    all_trips = trips.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('alltrips'))
            
            queries = Q(venue__icontains=query) | Q(description__icontains=query)
            all_trips = all_trips.filter(queries)

   # alltrips is the variable called in the html file to show the data eg {% url 'alltrips' %}
    context = {
        'alltrips': all_trips,
        'search_term': query,
    }

    return render(request, 'all_trips.html', context )

def det_trips_view(request, trips_id):
    """ A view to return detail of the product"""

    trip_details = get_object_or_404(trips, pk=trips_id)
    
   # Det_trips Is the variable called in the html file to show the data
    context = {
        'det_trips_view': trip_details,
    }

    return render(request, 'detail_trips.html', context ) 