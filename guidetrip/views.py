from django.shortcuts import render, get_object_or_404
from .models import trips

# Create your views here.
def all_trips(request):
    """ A view to return the all trips and show sorting and search result"""

    all_trips = trips.objects.all()
    
   # alltrips is the variable called in the html file so show the data
    context = {
        'alltrips': all_trips,
    }

    return render(request, 'all_trips.html', context )

def det_trips_view(request, trips_id):
    """ A view to return detail of the product"""

    trip_details = get_object_or_404(trips, pk=trips_id)
    
   # Det_trips Is the variable called in the html file so show the data
    context = {
        'det_trips_view': trip_details,
    }

    return render(request, 'detail_trips.html', context ) 