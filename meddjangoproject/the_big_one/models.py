from django.db import models


class Address(models.Model):
  # This table stores all the addresses for doctors
  # TODO pretty much change all this to use local flavor 

  street_address = models.CharField(max_length = 250)
  city = models.CharField(max_length = 150)
  state = models.CharField(max_length = 2)
  zip_code = models.CharField(max_length = 10)
  # street_number and street_name will be optional fields that can be used if
  # we need to decompose the address into its parts
  street_number = models.CharField(max_length = 15, blank = True)
  street_name = models.CharField(max_length = 200, blank = True)
  is_active = models.BooleanField(
      verbose_name = 'is address actively being used', 
      default = True)
  user_submitted = models.BooleanField(default = False)
  # Two time stamp fields
  # auto_now_add time stamps when it is first created
  date_entered = models.DateTimeField(
      verbose_name = 'date+time address entered', 
      auto_now_add = True)
  # auto_now time stamps when the field is saved
  date_last_updated = models.DateTimeField(
      verbose_name = 'date+time last changed', 
      auto_now = True)

  def __str__(self):
    self.full_address = self.street_address + '\n' + self.city + ', ' + \
        self.state + ' ' + self.zip_code


class Specialty(models.Model):
  # A model for storing the available specialties
  # TODO Refine the many-to-many replationship to express the membership of a
  # doctor in a specialty more effectively

  specialty_name = models.CharField(max_length = 250)

  def __str__(self):
    return self.specialty_name

class Doctor(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  # a doctor has one address, but multiple doctors can have same address
  # therefore, many-to-one replationship
  address = models.ForeignKey(Address, blank=True, null=True)
  # doctor can have multiple specialties and specialties can belong to 
  # multiple doctors therefore, many-to-many relationship
  specialties = models.ManyToManyField(Specialty)
  email_address = models.EmailField()
  # TODO change this to use localflavor
  phone_number = models.CharField(max_length = 9)
  # This field should be automatically calculated by a script nightly
  average_price = models.DecimalField(max_digits = 10, 
      blank = True, null = True, decimal_places = 2)

  def __str__(self):
    self.name = self.first_name + ' ' +  self.last_name
    return self.name


