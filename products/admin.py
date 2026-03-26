from django.contrib import admin

from .models import Product, Category, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'sale_price',
        'is_on_sale',
        'is_new',
        'is_featured',
        'is_deal_of_day',
        'is_highlighted',
        'stock_quantity',
        'rating',
        'image',
    )

    ordering = ('sku',)

    list_editable = (
        'is_featured',
        'is_deal_of_day',
        'is_highlighted',
        'is_on_sale',
        'is_new',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Offer)