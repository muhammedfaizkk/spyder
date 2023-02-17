from django.urls import path
from . import views

app_name = 'common'



urlpatterns=[    
   
    path('customersignup/',views.common_customersignup, name='common_customersignup'),
    path('login/',views.common_login, name='common_login'),
    path('sellerlogin/',views.common_sellerlogin, name='common_sellerlogin'),
    path('index/',views.common_index, name='common_index'),
    path('sellersignup/',views.common_sellersignup, name='common_sellersignup'),
    
    
    
    
    
    
    
    ]