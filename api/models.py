# api/models.py

from django.db import models

class Makeup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='makeup_images/', null=True, blank=True)  # Update upload path if necessary
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
