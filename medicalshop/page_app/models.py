from django.db import models
from django .contrib.auth.models import User

class Profile(models.Model):
    CHOICES=(
    ("ADMIN","ADMIN"),
    ("STAFF","STAFF"),
    ("CUSTOMER","CUSTOMER"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    type = models.CharField(max_length=150, choices = CHOICES, default = "STAFF")


class Category(models.Model):
    name= models.CharField(max_length=150)
    img= models.ImageField(upload_to='images/',blank=True,null=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    img = models.ImageField(upload_to='images/', default=None)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
   

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 

class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    
class Address(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField()