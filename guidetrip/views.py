from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import trips, categories
from .forms import ProductForm  # defined in forms.py not trips
from guideflyfishing.decorators import validate_guide


def all_trips(request):
    """ A view to return the all trips and show sorting and search result"""

    all_trips_rec = trips.objects.all()
    query = None
    category_list = None
    catobjects = None
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
            all_trips_rec = (all_trips_rec.filter
                             (categories__name__in=category_list))
            catobjects = categories.objects.filter(name__in=category_list)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't"
                                        " enter any search criteria!")
                return redirect(reverse('alltrips'))

            queries = (Q(venue__icontains=query)
                       | Q(description__icontains=query))
            all_trips_rec = trips.objects.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # alltrips is the defintion called in the html
    # file to show the data eg {% url 'alltrips' %}
    context = {
        'alltrips': all_trips_rec,
        'search_term': query,
        'current_catobject': catobjects,
        'current_sorting': current_sorting,
    }

    return render(request, 'all_trips.html', context)


def det_trips_view(request, trips_id):
    """ A view to return detail of the product"""

    trip_details = get_object_or_404(trips, pk=trips_id)

    # Det_trips Is the variable called in the html file to show the data
    context = {
        'det_trips_view': trip_details,
    }

    return render(request, 'detail_trips.html', context)


@login_required
# @validate_guide
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only guides '
                                'or store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            # Set rec_owner to the logged-in user,
            # for evaluation to edit update/add product
            product.rec_owner = request.user
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('det_trips_view', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. '
                                    'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
# @validate_guide
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only guides '
                                'or store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(trips, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('det_trips_view', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. '
                                    'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.venue}')

    template = 'edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
# @validate_guide
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only guides '
                                'or store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(trips, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('alltrips'))
