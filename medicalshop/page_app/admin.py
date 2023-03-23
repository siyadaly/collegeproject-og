from django.contrib import admin
from .models import Profile,Product,Order

class ProfileAdmin(admin.ModelAdmin):
    list_filter =("id","type")
    list_display =("id","type")

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Product)
admin.site.register(Order)
