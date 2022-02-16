from django.db import models
from config.constants import *
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


class Tshirt(models.Model):
    class Meta(object):
        db_table = 'tshirt'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=255
    )
    type = models.CharField(
        'Type', blank=False, null=False, max_length=255, choices=TYPE
    )
    price = models.FloatField(
        'Price', blank=False, null=False, max_length=255, validators=[MinValueValidator(1)]
    )
    size = models.CharField(
        'Size', blank=False, null=False, max_length=255, choices=SIZE
    )
    color_code = models.CharField(
        'Color', blank=False, null=False, max_length=50
    )
    image = CloudinaryField(
        'Image', blank=False, null=False
    )
    created_at = models.DateTimeField(
        'Creation Date', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Update Date', blank=True, auto_now=True
    )

    def __str__(self):
        return self.name
