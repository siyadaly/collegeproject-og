from django.shortcuts import render

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
    