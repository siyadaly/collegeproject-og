from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('product/', views.product,name='product'),
    path('purchase/', views.purchase,name='purchase'),
    path('about/', views.about,name='about'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    # customer
    path('customer/register/',views.customerregister,name="customerregister"),
    path('customer/login/',views.customer_login,name="customerlogin"),
    path('customer/home/',views.customerhome,name="customerhome"),
    #staff
    path('staff/register/',views.staffregister,name="staffregister"),
    path('staff/logout/',views.stafflogout,name="stafflogout"),
    path('staff/home/',views.staffhome,name="staffhome"),
    path('staff/add-product/',views.staff_add_product,name="staff-add-product"),







    
]
