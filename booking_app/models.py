from django.db import models

# Create your models here.

# Create your models here.
class BookingDetails(models.Model):
    name = models.TextField()
    age = models.TextField()
    user = models.CharField(max_length=100)
