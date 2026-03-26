from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all().prefetch_related('offers')
    query = None
    categories = None
    selected_category = 'all_products'
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if request.GET.get('direction') == 'desc':
                sortkey = f'-{sortkey}'
                direction = 'desc'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')

            if categories:
                selected_category = categories[0]

            if 'deals' in categories:
                products = products.filter(
                    Q(is_on_sale=True) |
                    Q(offers__is_active=True)
                ).distinct()

                categories = Category.objects.filter(
                    name__in=[
                        c for c in categories if c != 'deals'
                    ]
                )

            elif 'all_foods' in categories:
                food_categories = [
                    'whole_foods',
                    'frozen',
                    'meat_poultry',
                ]

                products = products.filter(
                    category__name__in=food_categories
                )

                categories = Category.objects.filter(
                    name__in=food_categories
                )

            elif 'all_drinks' in categories:
                drink_categories = [
                    'hot_beverages',
                    'cold_drinks',
                ]

                products = products.filter(
                    category__name__in=drink_categories
                )

                categories = Category.objects.filter(
                    name__in=drink_categories
                )

            else:
                products = products.filter(
                    category__name__in=categories
                )

                categories = Category.objects.filter(
                    name__in=categories
                )

        if 'q' in request.GET:
            query = request.GET['q']

            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )

            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    category_slugs = [
        'whole_foods',
        'frozen',
        'meat_poultry',
        'hot_beverages',
        'cold_drinks',
    ]

    category_story_products = {}

    for slug in category_slugs:
        product = Product.objects.filter(
            category__name=slug
        ).order_by('?').first()

        if product:
            category_story_products[slug] = product

    category_story_products['all_products'] = Product.objects.order_by(
        '?'
    ).first()

    category_story_products['all_foods'] = Product.objects.filter(
        category__name__in=[
            'whole_foods',
            'frozen',
            'meat_poultry',
        ]
    ).order_by('?').first()

    category_story_products['all_drinks'] = Product.objects.filter(
        category__name__in=[
            'hot_beverages',
            'cold_drinks',
        ]
    ).order_by('?').first()

    deal_story_product = Product.objects.filter(
        Q(is_on_sale=True) |
        Q(offers__is_active=True)
    ).distinct().order_by('?').first()

    product_names = (
        Product.objects.only('id', 'name')
        .order_by('?')[:80]
    )

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'category_story_products': category_story_products,
        'deal_story_product': deal_story_product,
        'selected_category': selected_category,
        'product_names': product_names,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    featured_products = (
        Product.objects.exclude(pk=product_id)
        .order_by('?')
        .prefetch_related('offers')[:12]
    )

    context = {
        'product': product,
        'featured_products': featured_products,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """Add a product to the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(
                reverse('product_detail', args=[product.id])
            )

        messages.error(
            request,
            'Failed to add product. Please ensure the form is valid.'
        )

    else:
        form = ProductForm()

    template = 'products/add_product.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(
                reverse('product_detail', args=[product.id])
            )

        messages.error(
            request,
            'Failed to update product. Please ensure the form is valid.'
        )

    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    messages.success(request, 'Product deleted!')

    return redirect(reverse('products'))
