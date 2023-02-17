from django.shortcuts import render

# Create your views here.
def eadmin_approveseller(request):
    return render(request,'spideradmintemp/approveseller.html')
def eadmin_index(request):
    return render(request,'spideradmintemp/index.html')  
def eadmin_login(request):
    return render(request,'spideradmintemp/login.html')  
def eadmin_removecustomer(request):
    return render(request,'spideradmintemp/removecustomer.html')
def eadmin_removepro(request):
    return render(request,'spideradmintemp/removepro.html')
def eadmin_removeseller(request):
    return render(request,'spideradmintemp/removeseller.html')
def eadmin_viewcustomer(request):
    return render(request,'spideradmintemp/viewcustomer.html')  
def eadmin_viewproducts(request):
    return render(request,'spideradmintemp/viewproducts.html')  
def eadmin_viewseller(request):
    return render(request,'spideradmintemp/viewseller.html')
