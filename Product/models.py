from django.db import models
from datetime import datetime
from Seller import models as seller_model
from Customer import models as customer_model


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)



class SubCategory(models.Model):
    category_name = models.ForeignKey(Category,related_name="categories",on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)


class ProductImage(models.Model):
    product_side_image = models.ImageField(upload_to="uploads/product/image/")
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    subcat_category = models.ForeignKey(SubCategory,related_name="subcat",on_delete=models.CASCADE)
    seller = models.ForeignKey(seller_model.Seller,related_name="seller",on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    product_image = models.ImageField(upload_to="uploads/product/image/")
    product_side_images = models.ManyToManyField(ProductImage,related_name="sideimages")
    actual_price = models.FloatField(default=0)
    discounted_price = models.FloatField(default=0)
    dimension = models.CharField(max_length=100)
    stock_quatity = models.IntegerField(default=0)
    color = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    

class ProductReview(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(customer_model.Customer,on_delete=models.CASCADE)
    feedback = models.TextField()
    rating = models.FloatField(default=0)
    review_image = models.ImageField(upload_to="uploads/product-review/image/",blank=True,null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)




