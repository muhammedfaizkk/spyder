from django.shortcuts import render

# Create your views here.
def customer_buy(request):
    return render(request,'customertemp/buy.html')
def customer_index(request):
    return render(request,'customertemp/index.html')  
def cutomer_mycart(request):
    return render(request,'customertemp/mycart.html')  
def customer_myorder(request):
    return render(request,'customertemp/myorder.html')
def customer_passwordchange(request):
    return render(request,'customertemp/passwordchange.html')
def customer_productdetails(request):
    return render(request,'customertemp/productdetails.html')
def customer_profile(request):
    return render(request,'customertemp/profile.html')  
def customer_update(request):
    return render(request,'customertemp/update.html')  

