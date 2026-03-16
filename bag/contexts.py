from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    offer_groups = {}

    for item_id, item_data in list(bag.items()):

        product = Product.objects.filter(pk=item_id).first()
        if not product:
            bag.pop(item_id, None)
            continue

        if isinstance(item_data, int):
            offer = product.offers.filter(is_active=True).first()
            if offer and offer.multi_buy_qty and offer.multi_buy_price:
                offer_groups.setdefault(offer.id, {'offer': offer, 'items': []})
                offer_groups[offer.id]['items'].append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'size': None,
                })
            else:
                line_subtotal = product.effective_price * item_data
                item_price = product.effective_price
                total += line_subtotal
                product_count += item_data
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'price_each': item_price,
                })
            
        else:
            for size, quantity in item_data['items_by_size'].items():
                offer = product.offers.filter(is_active=True).first()
                if offer and offer.multi_buy_qty and offer.multi_buy_price:
                    offer_groups.setdefault(offer.id, {'offer': offer, 'items': []})
                    offer_groups[offer.id]['items'].append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                    })
                else:
                    line_subtotal = product.effective_price * quantity
                    item_price = product.effective_price
                    total += line_subtotal
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                        'price_each': item_price,
                    })

    # Apply mix-and-match offers (split evenly across all eligible items)
    for group in offer_groups.values():
        offer = group['offer']
        items = group['items']
        total_qty = sum(item['quantity'] for item in items)
        if total_qty == 0:
            continue

        # Regular total based on effective prices
        regular_total = sum(
            item['product'].effective_price * item['quantity'] for item in items
        )

        bundles = total_qty // offer.multi_buy_qty
        remainder = total_qty % offer.multi_buy_qty
        avg_price = regular_total / total_qty
        total_cost = (bundles * offer.multi_buy_price) + (remainder * avg_price)
        blended_price = total_cost / total_qty

        for item in items:
            line_subtotal = blended_price * item['quantity']
            total += line_subtotal
            product_count += item['quantity']
            bag_items.append({
                'item_id': item['item_id'],
                'quantity': item['quantity'],
                'product': item['product'],
                'size': item['size'],
                'price_each': blended_price,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
