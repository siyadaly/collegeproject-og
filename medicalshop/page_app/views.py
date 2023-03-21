from django.shortcuts import render,redirect
from .forms import staffForm
from .forms import customerForm
from .models import Profile

# Create your views here.
def home(request):
    return render (request,'home.html')
def product(request):
    return render (request,'product.html')
def sale(request):
    return render (request,'sale.html')
def purchase(request):
    return render (request,'purchase.html')    
def about(request):
    return render (request,'about.html')
def login(request):

    return render (request,'login.html')  
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
    return render(request,'stafflogin.html')
def customer_login(request):
    return render(request,'customerlogin.html')
def staffhome(request):
    return render(request,'staffhome.html')
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
    