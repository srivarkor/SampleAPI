from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = PhoneNumberField()
    email = models.EmailField(max_length=255)
    def __str__(self):
        return self.firstName
