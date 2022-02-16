from django.db import models
from apps.products.models import Product
from apps.users.models import User
from config.constants import *
from django.core.validators import MinValueValidator


class Order(models.Model):
    class Meta(object):
        db_table = 'order'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True
    )
    total_price = models.FloatField(
        'Total Price', blank=False, null=False, max_length=255, validators=[MinValueValidator(1)]
    )
    full_name = models.CharField(
        'Full Name', blank=False, null=False, max_length=25, db_index=True
    )
    address_line1 = models.CharField(
        'Address Line1', blank=False, null=False, max_length=250, db_index=True
    )
    address_line2 = models.CharField(
        'Address Line2', blank=False, null=False, max_length=250, db_index=True
    )
    city = models.CharField(
        'City', blank=False, null=False, max_length=25, db_index=True
    )
    state = models.CharField(
        'State', blank=False, null=False, max_length=25, db_index=True
    )
    postal_code = models.IntegerField(
        'Postal Code', blank=False, null=False, db_index=True
    )
    country = models.CharField(
        'Country', blank=False, null=False, max_length=25, db_index=True, choices=COUNTRIES, default='United State'
    )
    telephone = models.IntegerField(
        'Telephone', blank=True, null=True, db_index=True
    )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )


class OrderItem(models.Model):
    class Meta(object):
        db_table = 'order_item'

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_index=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_index=True
    )
    quantity = models. IntegerField(
        'Quantity', blank=False, null=False, db_index=True
    )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )
