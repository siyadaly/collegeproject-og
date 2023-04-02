from django import forms
from django .contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product,Address

class staffForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(staffForm,self).__init__(*args,**kwargs)
        self.fields['username'].help_text=''
        self.fields['email'].help_text =''
        self.fields['password1'].help_text =''

    class Meta:
        model = User 
        fields = ('username','email','password1','password2')

class customerForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(customerForm,self).__init__(*args,**kwargs)
        self.fields['username'].help_text=''
        self.fields['email'].help_text =''
        self.fields['password1'].help_text =''

    class Meta:
        model = User 
        fields = ('username','email','password1','password2')


class ProductForm(forms.ModelForm):
      class Meta:
        model = Product
        fields = ('product_name','product_description', 'price', 'img','category' )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address',)