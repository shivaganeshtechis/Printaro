from django.db import models
from config.constants import *
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


class Logo(models.Model):
    class Meta(object):
        db_table = 'logo'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=255
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
