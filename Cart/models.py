from statistics import mode
from django.db import models
from datetime import datetime
from Customer import models as customer_model
from Product import models as product_model
from django.core.validators import MinValueValidator,MaxValueValidator


class CustomerCart(models.Model):
    user = models.ForeignKey(customer_model.Customer,on_delete=models.CASCADE)
    product_id = models.ForeignKey(product_model.Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    dimension = models.TextField(null=True,blank=True)
    color = models.CharField(max_length=100,null=True,blank=True)
    active = models.BooleanField(default=True)
    ispurchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

