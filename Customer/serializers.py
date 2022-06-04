from dataclasses import fields
from re import M
from rest_framework import serializers
from . import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        exclude = ("password",)

        