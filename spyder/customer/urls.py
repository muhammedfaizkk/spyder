from django.urls import path
from . import views

app_name = 'customer'



urlpatterns=[    
   
    path('buy/',views.customer_buy, name='customer_buy'),
    path('index/',views.customer_index, name='customer_index'),
    path('mycart/',views.cutomer_mycart, name='mycart'),
    path('myorder/',views.customer_myorder, name='customer_myorder'),
    path('passwordchange/',views.customer_passwordchange, name='customer_passwordchange'),
    path('productdetails/',views.customer_productdetails, name='customer_productdetails'),
    path('profile/',views.customer_profile, name='customer_profile'),
    path('update/',views.customer_update, name='customer_update'),
    
    
]
    
    
    
    
    
    