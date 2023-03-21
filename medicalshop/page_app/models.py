from django.db import models
from django .contrib.auth.models import User


# Create your models here.
#class staff(models.Model):
    #staff_name = models.TextField()
   # email =models.EmailField()
    #password =models.TextField()
    #staff_phonenumber = models.IntegerField()

#class product(models.Model):
    #product_name = models.TextField()
    #cost = models.IntegerField()
    #type = models.TextField()
    #product_Description = models.TextField()

#class order(models.Model):
   # productid = models.IntegerField()
    #ustomer_id = models.IntegerField()
    #created_on = models.DateTimeField(auto_now_add=True) 

#class cutomer(models.Model):
    #cus_email = models.EmailField(max_length=254)
    #cus_password = models.TextField()
    #cus_phonenumber =models.IntegerField()
    #cus_address = models.TextField()

#class payment(models.Model):
    #order_id = models.IntegerField()
   # cus_id = models.IntegerField()
    #cus_name = models.TextField()
    #cus_address = models.TextField()
    #Product_description = models.TextField()
    



# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", 'Admin'
#         STAFF = "STAFF", 'Staff'
#         CUSTOMER = "CUSTOMER", 'customer'
#     base_role = Role.ADMIN

#     role = models.CharField(max_length=20,choices=Role.choices)

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(args,*kwargs)
        

# class StaffManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.STAFF)

        
# class Staff(User):

#     base_role = User.Role.STAFF

#     teacher = StaffManager()


#     class Meta:
#         proxy = True


# @receiver(post_save, sender=Staff)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "STAFF":
#         StaffProfile.objects.create(user=instance)


# class StaffProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     student_id = models.IntegerField(null=True, blank=True)


# class CustomerManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.Customer)


# class Customer(User):

#     base_role = User.Role.CUSTOMER

#     teacher = CustomerManager()

#     class Meta:
#         proxy = True


# class CustomerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     teacher_id = models.IntegerField(null=True, blank=True)


# @receiver(post_save, sender=Customer)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "TEACHER":
#         CustomerProfile.objects.create(user=instance)

class Profile(models.Model):
    CHOICES=(
    ("ADMIN","ADMIN"),
    ("STAFF","STAFF"),
    ("CUSTOMER","CUSTOMER"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    type = models.CharField(max_length=150, choices = CHOICES, default = "STAFF")
