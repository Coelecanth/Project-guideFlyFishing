from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import trips, categories

# Create your views here.
def all_trips(request):
    """ A view to return the all trips and show sorting and search result"""

    all_trips_rec = trips.objects.all()
    query = None
    category_list = None 
    catobjects  = None
    sort = None
    direction = None
    tripfilter = None
    
    if request.GET:
        if 'sort' in request.GET:
            print("Request: ", request)
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'venue':
                sortkey = 'lower_name'
                catobjects = all_trips_rec.annotate(lower_name=Lower('venue'))
                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                catobjects = all_trips_rec.order_by(sortkey)
            all_trips_rec = all_trips_rec.order_by(sortkey)
        
        if 'category' in request.GET:
            category_list = request.GET['category'].split(',')
            all_trips_rec = all_trips_rec.filter(categories__name__in=category_list)
            catobjects  = categories.objects.filter(name__in=category_list)
         

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('alltrips'))
            
            queries = Q(venue__icontains=query) | Q(description__icontains=query)
            all_trips_rec = trips.objects.filter(queries)

    current_sorting = f'{sort}_{direction}'
  
  
   # alltrips is the defintion called in the html file to show the data eg {% url 'alltrips' %}
    context = {
        'alltrips': all_trips_rec,
        'search_term': query,
        'current_catobject': catobjects,
        'current_sorting': current_sorting,
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