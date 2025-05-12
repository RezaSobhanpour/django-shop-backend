import os.path
import random

from django.db import models

from category_shop.models import Category
from color_shop.models import ClotheColor
from size_shop.models import ClotheSize


def get_file_extension(file):
    basename = os.path.basename(file)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_image(instance, file):
    rand_name = random.randint(1, 999)
    name, ext = get_file_extension(file)
    new_name = f"{instance.id}_{rand_name}{ext}"
    return new_name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    price = models.IntegerField()
    exists = models.BooleanField(default=False)
    color = models.ManyToManyField(ClotheColor)
    size = models.ManyToManyField(ClotheSize)
    category = models.ManyToManyField(Category)
    special = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    sold = models.IntegerField(default=0)

    def __str__(self):
        return self.title
