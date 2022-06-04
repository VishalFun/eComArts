from rest_framework import generics
from . import models
from . import serializers

class CustomerListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer