import os.path
import random

from django.db import models


def get_file_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


def partner_upload_image(instance, filename):
    rand = random.randint(1, 999)
    name, ext = get_file_ext(filename)
    new_name = f"aboutus/{instance.id}_{name}_{rand}{ext}"
    return new_name


def company_logo_upload_image(instance, filename):
    rand = random.randint(1, 999)
    name, ext = get_file_ext(filename)
    new_name = f"logo/{instance.id}_{name}_{rand}{ext}"
    return new_name


def social_logo_upload_image(instance, filename):
    rand = random.randint(1, 999)
    name, ext = get_file_ext(filename)
    new_name = f"logo/{instance.id}_{name}_{rand}{ext}"
    return new_name


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    logo = models.ImageField(upload_to=company_logo_upload_image, blank=True, null=True)

    email = models.EmailField(null=True)

    def save(self, *args, **kwargs):
        if AboutUs.objects.exists():
            ValueError("There can be only one instance of AboutUs")
        super().save(*args, **kwargs)


class Partners(models.Model):
    name = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
    partner_description = models.TextField()
    role_description = models.TextField()
    image = models.ImageField(upload_to=partner_upload_image, blank=True, null=True)
    AboutUs = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='partners')

    def __str__(self):
        return self.name


class Link(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=social_logo_upload_image, blank=True, null=True)
    url = models.URLField()
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='links', null=True, blank=True)

    def __str__(self):
        return self.title
