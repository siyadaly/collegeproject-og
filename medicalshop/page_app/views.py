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