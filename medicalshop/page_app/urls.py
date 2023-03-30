from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('product/', views.product,name='product'),
    path('about/', views.about,name='about'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    # customer
    path('customer/register/',views.customerregister,name="customerregister"),
    path('customer/login/',views.customer_login,name="customerlogin"),
    path('customer/home/',views.customerhome,name="customerhome"),
    path('customer/logout/',views.customerlogout,name="customerlogout"),
    #staff
    path('staff/register/',views.staffregister,name="staffregister"),
    path('staff/login/',views.staff_login,name="stafflogin"),
    path('staff/logout/',views.stafflogout,name="stafflogout"),
    path('staff/home/',views.staffhome,name="staffhome"),
    path('staff/add-product/',views.staff_add_product,name="staff-add-product"),
    path('staff/order/',views.stafforder,name="stafforder"),
    path('customer/order/',views.customer_order,name="customer_order"),
    path('customer/order/<int:id>',views.order,name="add_order"),
    path('addtocart/',views.cart,name="add_tocart"),
    path('addtocart/<int:id>',views.add_to_cart,name="add_cart"),










    
]
