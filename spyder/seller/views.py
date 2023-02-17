from django.shortcuts import render

# Create your views here.
def seller_addproduct(request):
    return render(request,'resellertemp/addproduct.html')
def seller_changepassword(request):
    return render(request,'resellertemp/changepassword.html')  
def seller_index(request):
    return render(request,'resellertemp/index.html')  
def seller_productcatelogue(request):
    return render(request,'resellertemp/productcatelogue.html')
def seller_profile(request):
    return render(request,'resellertemp/profile.html')
def seller_recentorders(request):
    return render(request,'resellertemp/recentorders.html')
def seller_update(request):
    return render(request,'resellertemp/update.html')  
def seller_updatestock(request):
    return render(request,'resellertemp/updatestock.html')  

