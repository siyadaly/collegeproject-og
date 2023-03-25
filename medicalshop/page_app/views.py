from django.shortcuts import render,redirect
from .forms import staffForm,customerForm,ProductForm
from .models import Profile, Category, Product
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator


# Create your views here.
def is_staff(user):    
     try:       
        return user.is_authenticated and (user.profile.type == 'STAFF')     
     except Profile.DoesNotExist:       
         return False     
def is_customer(user):     
    try:         
         return user.is_authenticated and (user.profile.type == 'CUSTOMER' )    
    except Profile.DoesNotExist:         
            return False


def purchase(request):
    return render (request,'purchase.html')    
def about(request):
    return render (request,'about.html')
 
def register(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname= request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeatpassword = request.POST.get("Repeatpassword")
        print(firstname)
        print(lastname)
        print(email)
        print(password)
        print(repeatpassword)
    return render(request,'register.html')  


def staff_login(request):
    if request .method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if(user.profile.type == 'CUSTOMER'):
                    return redirect("stafflogin")
                else:
                    return redirect("staffhome")
    else:
        form = AuthenticationForm()
    return render(request,'stafflogin.html',{'form':form})

def customer_login(request):
    if request .method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if(user.profile.type == 'STAFF'):
                    return redirect("customerlogin")
                else:
                    return redirect("customerhome")
    else:
        form = AuthenticationForm()
    return render(request,'customerlogin.html',{'form':form})


@user_passes_test(is_customer,login_url='/customer/login/')
def customerhome(request):
    return render(request,'customerhome.html')
def customerregister(request):
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.type = 'CUSTOMER'
            profile.user =user
            profile.save()
            return redirect('customerlogin')
    else:
        form = staffForm()
    return render(request,'customerregister.html',{'form':form})
def staffregister(request):
    if request.method == 'POST':
        form =staffForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.type = 'STAFF'
            profile.user =user
            profile.save()
            return redirect('stafflogin')
    else:
        form = staffForm()
    return render(request,'staffregister.html',{'form':form})
def stafflogout(request):
    logout(request)
    return redirect('stafflogin')
def customerlogout(request):
    logout(request)
    return redirect('customerlogin')


# CUSTOMER

def home(request):
    if request.method == 'POST':
        search  = request.POST['search']
        return redirect(f'/product?search={search}')
    
    categories = Category.objects.all()
    data ={
        "categories":categories
    }
    
    return render (request,'home.html',data)

def product(request):
    categoryID = request.GET.get('category')
    search = request.GET.get('search')
    if categoryID:
        products = Product.objects.filter(category=categoryID)
        category = Category.objects.filter(id=categoryID)[0]
    elif search:
        products = Product.objects.filter(product_name__contains=search)
        category = None
    else:
        products = Product.objects.all()
        category = None
    pagination = Paginator(products,10)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    data ={
        "products":products,
        "page_obj":page_obj,
        "category":category
    }
    return render (request,'product.html',data)



# STAFF

# @user_passes_test(is_staff,login_url='/staff/login/')
def staffhome(request):
    products = Product.objects.all()
    pagination = Paginator(products,10)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    data ={
        "products":products,
        "page_obj":page_obj

    }
    return render(request,'staffhome.html',data)

def staff_add_product(request):
     
    if request.method == 'POST':
        product_form = ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            product= Product()
            product.product_name = product_form.cleaned_data['product_name']
            product.product_description = product_form.cleaned_data['product_description']
            product.price =product_form.cleaned_data['price']
            product.img = product_form.cleaned_data['img']
            product.category = product_form.cleaned_data['category']
            product.save()
    else:
        product_form = ProductForm()

    data ={
        "product_form":product_form
    }

    return render(request, 'staffaddproduct.html',data)