from django.urls import path
from . import views

app_name = 'seller'



urlpatterns=[    
   
    path('addproduct/',views.seller_addproduct, name='seller_addproduct'),
    path('changepassword/',views.seller_changepassword, name='seller_changepassword'),
    path('index/',views.seller_index, name='seller_index'),
    path('productcatelogue/',views.seller_productcatelogue, name='seller_productcatelogue'),
    path('profile/',views.seller_profile, name='seller_profile'),
    path('recentorders/',views.seller_recentorders, name='seller_recentorders'),
    path('update/',views.seller_update, name='seller_update'),
    path('updatestock/',views.seller_updatestock, name='seller_updatestock'),
    
    
    
    
    
    
    
    
    ]