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
    path('staff/login/',views.staff_login,name="stafflogin"),
    path('customer/login/',views.customer_login,name="customerlogin"),
    path('staff/home/',views.staffhome,name="staffhome"),
    path('customer/home/',views.customerhome,name="customerhome"),
    path('customer/register/',views.customerregister,name="customerregister"),
    path('staff/register/',views.staffregister,name="staffregister"),




    
]
