from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()

    def __str__(self):
        return self.email
