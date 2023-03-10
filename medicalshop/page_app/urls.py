from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('product/', views.product,name='product'),
    path('sale/', views.sale,name='sale'),
    path('purchase/', views.purchase,name='purchase'),
    path('about/', views.about,name='about'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
      
]
