from django.urls import path
from . import views

app_name = 'eco_admin'



urlpatterns=[    
   
    path('approveseller/',views.eadmin_approveseller, name='eadmin_approveseller'),
    path('index/',views.eadmin_index, name='eadmin_index'),
    path('login/',views.eadmin_login, name='eadmin_login'),
    path('removecustomer/',views.eadmin_removecustomer, name='eadmin_removecustomer'),
    path('removepro/',views.eadmin_removepro, name='eadmin_removepro'),
    path('removeseller/',views.eadmin_removeseller, name='eadmin_removeseller'),
    path('viewcustomer/',views.eadmin_viewcustomer, name='eadmin_viewcustomer'),
    path('viewproducts/',views.eadmin_viewproducts, name='eadmin_viewproducts'),
    path('viewseller/',views.eadmin_viewseller, name='eadmin_viewseller'),
    
    
    
    
    
    
    
    ]