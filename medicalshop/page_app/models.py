from django.db import models


# Create your models here.
class staff(models.Model):
    staff_name = models.TextField()
    email =models.EmailField()
    password =models.TextField()
    staff_phonenumber = models.IntegerField()

class product(models.Model):
    product_name = models.TextField()
    cost = models.IntegerField()
    type = models.TextField()
    product_Description = models.TextField()

class order(models.Model):
    productid = models.IntegerField()
    order_name = models.TextField()
    customer_id = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True) 

class cutomer(models.Model):
    cus_email = models.EmailField(max_length=254)
    cus_name = models.TextField()
    cus_password = models.TextField()
    cus_phonenumber =models.IntegerField()
    cus_address = models.TextField()

class payment(models.Model):
    order_id = models.IntegerField()
    cus_id = models.IntegerField()
    cus_name = models.TextField()
    cus_address = models.TextField()
    product_description = models.TextField()



    
