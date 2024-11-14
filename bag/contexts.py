from django.shortcuts import get_object_or_404
from guidetrip.models import trips


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    grand_total = 0

    for item_id, quantity in bag.items():
        product = get_object_or_404(trips, pk=item_id)
        total += quantity * product.cost
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

        grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
    