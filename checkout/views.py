from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('alltrips'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QACArGBGDhYPnfDRAmNu9gVUc0FwdhsSXAz3vL98jeZrttgDWLnVNXbhaAicFY9OuByz9AoW1veFKRuxGAvPlRk00yW0Uh2dH',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
