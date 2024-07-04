from django.db import models
from .choices import COUNTRY_CHOICES

# Create your models here.
class Record(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return (f"{self.first_name} {self.last_name}" )