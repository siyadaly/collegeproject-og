from django.db import models


# Create your models here.
class staff(models.Model):
    staff_name =models.varchar(255)
    email =models.varchar(255)
    password =models.varchar(255)
    staff_phonenumber = models.varchar(10)

class product(models.Model):
    product_name = models.varchar(255)
    cost = models.varchar(255)
    type = models.varchar(255)
    product_Description = models.TextField()

class order(models.Model):
    productid = models.int()
    order_name = models.varchar(255)
    customer_id = models.int()
    created_on = models.DateTimeField(auto_now=true, auto_now_add=true) 

class cutomer(models.Model):
    cus_email = models.varchar(255)
    cus_name = models.varchar(255)
    cus_password = models.varchar(255)
    cus_phonenumber = models.varchar(10)
    cus_address = models.varchar(255)

class payment(models.Model):
    order_id = models.varchar(255)
    cus_id = models.varchar(255)
    cus_name = models.varchar(255)
    cus_address = models.varchar(255)
    product_description = models.TextField()



    
