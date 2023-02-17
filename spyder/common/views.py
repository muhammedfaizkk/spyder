from django.shortcuts import render

from common.models import Cutomer

# Create your views here.
def common_index(request):
    return render(request,'common_temp/index.html')
def common_customersignup(request):
    if request.method == 'POST':
        customer_name = request.POST['c_name']
        customer_gender = request.POST['c_gender']
        customer_email = request.POST['c_email']
        customer_phone = request.POST['phone']
        customer_address= request.POST['c_address']
        customer_password= request.POST['pass']
        customer_image= request.FILES['img']

        new_customer = Cutomer(
            customer_name = customer_name,
            gender = customer_gender,
            email     = customer_email ,
            customer_phonenumber =  customer_phone,
            customer_address = customer_address,
            customer_password = customer_password ,
            customer_image = customer_image 

        ) 
        new_customer.save()

def customer_login(request):
    msg = ''
    if request.method == 'POST':
       cust_email = request.POST['custid']
       cust_psw = request.POST['psw']
    try:
      customer = Customer.objects.get(e_mail = cust_email,password = )
      request.session['customer'] = customer.id
      return redirect('customer:home')
    except:
            msg = "Invalid Email ID or Password"
   




    return render(request,'common_temp/customersignup.html')  
def common_login(request):
    return render(request,'common_temp/login.html')  
def common_sellerlogin(request):
    return render(request,'common_temp/sellerlogin.html')
def common_sellersignup(request):
    return render(request,'common_temp/sellersignup.html')