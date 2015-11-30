from django.db import models

class Doctor(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)

class Address(models.model):
    street_address = models.CharField(max_length = 250)
    city = models.CharField(max_length = 150)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 5)


# Create your models here.
