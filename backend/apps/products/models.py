
from django.db.models.deletion import CASCADE
from django.db import models
from config.constants import *
from apps.tshirts.models import Tshirt
from apps.logos.models import Logo
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


class Product(models.Model):
    class Meta(object):
        db_table = 'product'

    tshirt = models.ForeignKey(
        Tshirt, on_delete=CASCADE, db_index=True
    )
    logo = models.ForeignKey(
        Logo, on_delete=CASCADE, db_index=True
    )
    name = models.CharField(
        'Name', blank=False, null=False, max_length=255, db_index=True
    )
    gender = models.CharField(
        'Gender', blank=False, null=False, max_length=255, choices=GENDER
    )
    price = models.FloatField(
        'Price', blank=False, null=False, max_length=255, validators=[MinValueValidator(1)]
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
