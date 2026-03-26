from decimal import Decimal
from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=254)
    description = models.TextField()

    brand = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    weight = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )

    has_sizes = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    sale_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    is_on_sale = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_deal_of_day = models.BooleanField(default=False)
    is_highlighted = models.BooleanField(default=False)

    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    unit_label = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )

    stock_quantity = models.IntegerField(default=0)

    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    review_count = models.IntegerField(default=0)

    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    @property
    def display_price(self):
        if self.is_on_sale and self.sale_price:
            return self.sale_price
        return self.price

    @property
    def has_discount(self):
        return (
            self.is_on_sale
            and self.sale_price
            and self.sale_price < self.price
        )

    @property
    def deal_price(self):
        if self.is_deal_of_day:
            return self.price * Decimal('0.70')
        return None

    @property
    def percent_off(self):
        if self.has_discount and self.price:
            discount = (
                (self.price - self.sale_price)
                / self.price * Decimal('100')
            )
            return int(discount.quantize(Decimal('1')))
        return 0

    @property
    def effective_price(self):
        if self.is_deal_of_day:
            return self.deal_price
        if self.has_discount:
            return self.sale_price
        return self.price

    def offer_subtotal(self, quantity):
        """
        Calculate subtotal applying the first active
        multi-buy offer, if any.
        """
        offer = self.offers.filter(is_active=True).first()

        if not offer or not offer.multi_buy_qty or not offer.multi_buy_price:
            return self.effective_price * quantity

        bundle_qty = offer.multi_buy_qty
        bundle_price = offer.multi_buy_price

        bundles = quantity // bundle_qty
        remainder = quantity % bundle_qty

        return (
            (bundles * bundle_price)
            + (remainder * self.effective_price)
        )


class Offer(models.Model):

    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    badge_text = models.CharField(
        max_length=60,
        null=True,
        blank=True
    )

    multi_buy_qty = models.IntegerField(default=0)

    multi_buy_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    products = models.ManyToManyField(
        Product,
        related_name='offers',
        blank=True
    )

    def __str__(self):
        return self.name