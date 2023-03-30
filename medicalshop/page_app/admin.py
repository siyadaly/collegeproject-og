from django.contrib import admin
from .models import Profile,Product,Order,Category,Cart

class ProfileAdmin(admin.ModelAdmin):
    list_filter =("id","type")
    list_display =("id","type")

admin.site.register(Profile,ProfileAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_filter =("id","name",)
    list_display =("id","name")

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_filter =("id","product_name","category")
    list_display =("id","product_name","category")

admin.site.register(Product,ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_filter =("id","product_name","category")
    list_display =("id","product_name","category")

admin.site.register(Order)

admin.site.register(Cart)
