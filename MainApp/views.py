from django.shortcuts import redirect, render
from django.contrib import messages
from MainApp.models import UserDetails,Headphones,phones,speakers,tvs,watches,Keyboards,mouse,laptops
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from datetime import datetime


# Create your views here.
def LandingPage(request):
    return render (request,'landing.html')

def SignupPage(request):
    if request.method=="POST":
        type=request.POST.get('form-type')
       
        if type=='login':
            email=request.POST.get('email1')
            pass1=request.POST.get('pass1')
            usermode=request.POST.get('login-type')

           
            if pass1=="" or  email=="":
             messages.warning(request,"All Fields Are Mandetory To Fill !!!")
             
            else:
               user=authenticate(request,username=email,password=pass1)
               if user is not None:
                    login(request,user)
                    print(request.user)
                    y=UserDetails.objects.filter(email=request.user)
                    print(usermode)
                    if usermode=="seller":
                        return redirect('sellerhome')
                    if usermode=="vendor":
                        return redirect('vednorhome')
                    if usermode=="organization":
                        return redirect('orghome')
                    


                    
               else:
                  messages.warning(request,"Username Or Password Is Incorrect !")
                  
        
            return redirect('signup')
        else:
            
            email=request.POST.get('email2')
            pass1=request.POST.get('pass2')
            pin=request.POST.get('pin')
            phone=request.POST.get('phone2')
            name=request.POST.get('name2')
          
        
            if pass1=="" or  email=="" or pin=="" or phone=="" or name=="":
             messages.warning(request,"All Fields Are Mandetory To Fill !!!")
             return redirect('signup')
            else:
               try:
                my_user=User.objects.create_user(email,email,pass1)
                my_user.save()
                data=UserDetails(name=name,email=email,pin=pin,phone=phone)
                data.save();
                messages.success(request,"Registration  Succesful!! , You Can Now LogIn To System ")
                return redirect('signup')
               except IntegrityError:
                messages.success(request,"Username Already Exists !!")
                return redirect('signup')

        
    return render (request,'signup.html')



def SellerHomePage(request):
   return render(request,'sellerhome.html')
def VendorHomePage(request):
        y=UserDetails.objects.filter(email=request.user)
        pin=0
        for i in y:
           pin=i.pin
        headphone=Headphones.objects.all().filter(userpin=pin)
        phone=phones.objects.all().filter(userpin=pin)
        tv=tvs.objects.all().filter(userpin=pin)
        speaker=speakers.objects.all().filter(userpin=pin)
        watch=watches.objects.all().filter(userpin=pin)
        keyboard=Keyboards.objects.all().filter(userpin=pin)
        m=mouse.objects.all().filter(userpin=pin)
        laptop=laptops.objects.all().filter(userpin=pin)
        return render (request,'vendorhome.html',{'headphone':headphone,'phone':phone,'tv':tv,'speaker':speaker,'watch':watch,'keyboard':keyboard,'mouse':m,'laptop':laptop})
  
def OrgHomePage(request):
   return render(request,'orghome.html')

def SellerOrderPage(request):
    if request.method=='GET':
        headphone=Headphones.objects.all().filter(userid=request.user)
        phone=phones.objects.all().filter(userid=request.user)
        tv=tvs.objects.all().filter(userid=request.user)
        speaker=speakers.objects.all().filter(userid=request.user)
        watch=watches.objects.all().filter(userid=request.user)
        keyboard=Keyboards.objects.all().filter(userid=request.user)
        m=mouse.objects.all().filter(userid=request.user)
        laptop=laptops.objects.all().filter(userid=request.user)
        return render (request,'sellerorder.html',{'headphone':headphone,'phone':phone,'tv':tv,'speaker':speaker,'watch':watch,'keyboard':keyboard,'mouse':m,'laptop':laptop})
    
       
    return render (request,'sellerorder.html')
def SellHeadphonePage(request):
    if request.method == 'POST':
        model=request.POST.get('selected_model_name');
        company=request.POST.get('selected_company_name');
        price=request.POST.get('newprice');
        condition=request.POST.get('condition_value');
        add=request.POST.get('address');
        image_view=request.FILES['image']
        y=UserDetails.objects.filter(email=request.user)
        current_datetime = datetime.now()
        for i in y:
          data=Headphones(userid=i.email,userpin=i.pin,name=i.name,phone=i.phone,company_name=company,price=price,model_no=model,status="Order Submitted ",overall_condition=condition,image1=image_view,address=add,order_date=current_datetime,expected_date=None)
          data.save()
        
        
        
     
    return render (request,'sellheadphone.html')
def SellPhonePage(request):
     if request.method == 'POST':
        model=request.POST.get('selected_model_name');
        company=request.POST.get('selected_company_name');
        price=request.POST.get('newprice');
        condition=request.POST.get('condition_value');
        add=request.POST.get('address');
        image_view=request.FILES['image']
        y=UserDetails.objects.filter(email=request.user)
        current_datetime = datetime.now()
        for i in y:
          data=phones(userid=i.email,userpin=i.pin,name=i.name,phone=i.phone,company_name=company,price=price,model_no=model,status="Order Submitted ",overall_condition=condition,image1=image_view,address=add,order_date=current_datetime,expected_date=None)
          data.save()
     return render (request,'sellphone.html')
def SellTvPage(request):
     if request.method == 'POST':
        model=request.POST.get('selected_model_name');
        company=request.POST.get('selected_company_name');
        price=request.POST.get('newprice');
        condition=request.POST.get('condition_value');
        add=request.POST.get('address');
        image_view=request.FILES['image']
        y=UserDetails.objects.filter(email=request.user)
        current_datetime = datetime.now()
        for i in y:
          data=tvs(userid=i.email,userpin=i.pin,name=i.name,phone=i.phone,company_name=company,price=price,model_no=model,status="Order Submitted ",overall_condition=condition,image1=image_view,address=add,order_date=current_datetime,expected_date=None)
          data.save()
     return render (request,'selltv.html')
def SellLaptopPage(request):
     if request.method == 'POST':
        model=request.POST.get('selected_model_name');
        company=request.POST.get('selected_company_name');
        price=request.POST.get('newprice');
        condition=request.POST.get('condition_value');
        image_view=request.FILES['image']
        add=request.POST.get('address');
        y=UserDetails.objects.filter(email=request.user)
        current_datetime = datetime.now()
        for i in y:
          data=laptops(userid=i.email,userpin=i.pin,name=i.name,phone=i.phone,company_name=company,price=price,model_no=model,status="Order Submitted ",overall_condition=condition,image1=image_view,address=add,order_date=current_datetime,expected_date=None)
          data.save()
     return render (request,'selllaptop.html')
def SellWatchPage(request):
     if request.method == 'POST':
        model=request.POST.get('selected_model_name');
        company=request.POST.get('selected_company_name');
        price=request.POST.get('newprice');
        condition=request.POST.get('condition_value');
        image_view=request.FILES['image']
        add=request.POST.get('address');
        y=UserDetails.objects.filter(email=request.user)
        current_datetime = datetime.now()
        for i in y:
          data=watches(userid=i.email,userpin=i.pin,name=i.name,phone=i.phone,company_name=company,price=price,model_no=model,status="Order Submitted ",overall_condition=condition,image1=image_view,address=add,order_date=current_datetime,expected_date=None)
          data.save()
     return render (request,'sellwatch.html')
def SellSpeakerPage(request):
     if request.method == 'POST':
        model=request.POST.get('selected_model_name');
        company=request.POST.get('selected_company_name');
        price=request.POST.get('newprice');
        condition=request.POST.get('condition_value');
        add=request.POST.get('address');
        image_view=request.FILES['image']
        y=UserDetails.objects.filter(email=request.user)
        current_datetime = datetime.now()
        for i in y:
          data=speakers(userid=i.email,userpin=i.pin,name=i.name,phone=i.phone,company_name=company,price=price,model_no=model,status="Order Submitted ",overall_condition=condition,image1=image_view,address=add,order_date=current_datetime,expected_date=None)
          data.save()
     return render (request,'sellspeaker.html')
def SellMousePage(request):
     if request.method == 'POST':
        model=request.POST.get('selected_model_name');
        company=request.POST.get('selected_company_name');
        price=request.POST.get('newprice');
        condition=request.POST.get('condition_value');
        add=request.POST.get('address');
        image_view=request.FILES['image']
        y=UserDetails.objects.filter(email=request.user)
        current_datetime = datetime.now()
        for i in y:
          data=mouse(userid=i.email,userpin=i.pin,name=i.name,phone=i.phone,company_name=company,price=price,model_no=model,status="Order Submitted ",overall_condition=condition,image1=image_view,address=add,order_date=current_datetime,expected_date=None)
          data.save()
     return render (request,'sellmouse.html')
def SellKeyboardPage(request):
     if request.method == 'POST':
        model=request.POST.get('selected_model_name');
        company=request.POST.get('selected_company_name');
        price=request.POST.get('newprice');
        condition=request.POST.get('condition_value');
        image_view=request.FILES['image']
        add=request.POST.get('address');
        y=UserDetails.objects.filter(email=request.user)
        current_datetime = datetime.now()
        for i in y:
          data=Keyboards(userid=i.email,userpin=i.pin,name=i.name,phone=i.phone,company_name=company,price=price,model_no=model,status="Order Submitted ",overall_condition=condition,image1=image_view,address=add,order_date=current_datetime,expected_date=None)
          data.save()
     return render (request,'sellkeyboard.html')