from django.shortcuts import render
from django.db.models import Q
from products.models import Product

# Create your views here.

def index(request):
    """ A view to return the index page """
    deal_product = Product.objects.filter(is_deal_of_day=True).first()
    highlighted_product = Product.objects.filter(is_highlighted=True).first()
    featured_products = (
        Product.objects.order_by('?')
        .prefetch_related('offers')[:12]
    )
    product_names = list(
        Product.objects.values_list('name', flat=True).order_by('name')
    )
    category_slugs = [
        'whole_foods',
        'frozen',
        'meat_poultry',
        'hot_beverages',
        'cold_drinks',
        'all_foods',
        'all_drinks',
    ]
    category_story_products = {}
    for slug in category_slugs:
        product = Product.objects.filter(category__name=slug).order_by('?').first()
        if product:
            category_story_products[slug] = product

    category_story_products['all_products'] = Product.objects.order_by('?').first()
    deal_story_products = (
        Product.objects.filter(is_on_sale=True) |
        Product.objects.filter(offers__is_active=True)
    ).distinct().order_by('?')
    deals_products = (
        Product.objects.filter(Q(is_on_sale=True) | Q(offers__is_active=True))
        .distinct()
        .prefetch_related('offers')
    )
    context = {
        'deal_product': deal_product,
        'highlighted_product': highlighted_product,
        'featured_products': featured_products,
        'category_story_products': category_story_products,
        'deal_story_product': deal_story_products.first(),
        'deals_products': deals_products,
        'product_names': product_names,
    }

    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def privacy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy.html')


def terms(request):
    """ A view to return the terms page """

    return render(request, 'home/terms.html')
