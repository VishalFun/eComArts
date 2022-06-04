from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractBaseUser


class Customer(AbstractBaseUser):
    email = models.EmailField(max_length=100,validators=[MinLengthValidator(3)],unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    pincode = models.CharField(max_length=16)
    state = models.CharField(max_length=100,validators=[MinLengthValidator(3)])
    city = models.CharField(max_length=100,validators=[MinLengthValidator(3)])
    contact = models.CharField(max_length=10,unique=True,validators=[MinLengthValidator(10)])
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=datetime.now)
    
    USERNAME_FIELD = "first_name"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

