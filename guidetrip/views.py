from django.shortcuts import render
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

 