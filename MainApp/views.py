from django.shortcuts import redirect, render
from django.contrib import messages
from MainApp.models import UserDetails,Headphones,phones,speakers,tvs,watches,Keyboards,mouse,laptops,VendorStocks
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from datetime import datetime, timedelta, timezone


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
                        vendor_exists = VendorStocks.objects.filter(vendor_id=request.user).exists()
                        if not vendor_exists:
                           for i in y:
                              data=VendorStocks(vendor_id=i.email,pin=i.pin,phone=i.phone)
                              data.save()
                           
                     

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
     if request.method=="POST":
      update=request.POST.get('status_change');
      orderid=request.POST.get('order');
      product_type=request.POST.get('product');
      condition=request.POST.get('condition');
      price=request.POST.get('price');
      print("Update : ",  update)
      print(orderid)
      print(product_type)
      print(condition)
      print(price)
      y=VendorStocks.objects.get(vendor_id=request.user)
      if update=="A":
         update="Accepted"
      if update=="C":
         update="Completed"
      if product_type=="headphone":
         order = Headphones.objects.get(id=orderid)
         order.status = update
         if update!="Completed" : order.expected_date = datetime.now() + timedelta(days=4)
         else:
             if condition=="good":
                  
                   y.good_headphone_stocks+=1; 
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.good_headphone_worth+=price_float
             elif condition=="best":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.best_headphone_worth+=price_float
                   y.best_headphone_stocks+=1; 
             else:
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.poor_headphone_worth+=price_float
                   y.poor_headphone_stocks+=1; 
         y.save()
         order.save()
      
      if product_type=="laptop":
         order = laptops.objects.get(id=orderid)
         order.status = update
         if update!="Completed" : order.expected_date = datetime.now() + timedelta(days=4)
         else:
             if condition=="good":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.good_laptop_worth+=price_float
                   y.good_laptop_stocks+=1; 
             elif condition=="best":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.best_laptop_worth+=price_float
                   y.best_laptop_stocks+=1; 
             else:
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.poor_laptop_worth+=price_float
                   y.poor_laptop_stocks+=1; 
         y.save()
         order.save()
         order.save()
      if product_type=="phone":
         order = phones.objects.get(id=orderid)
         order.status = update
         if update!="Completed" : order.expected_date = datetime.now() + timedelta(days=4)
         else:
             if condition=="good":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.good_phone_worth+=price_float
                   y.good_phone_stocks+=1; 
             elif condition=="best":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.best_phone_worth+=price_float
                   y.best_phone_stocks+=1; 
             else:
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.poor_phone_worth+=price_float
                   y.poor_phone_stocks+=1; 
         y.save()
         order.save()
         
      if product_type=="keyboard":
         order = Keyboards.objects.get(id=orderid)
         order.status = update
         if update!="Completed" : order.expected_date = datetime.now() + timedelta(days=4)
         else:
             if condition=="good":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.good_keyboard_worth+=price_float
                   y.good_keyboard_stocks+=1; 
             elif condition=="best":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.best_keyboard_worth+=price_float
                   y.best_keyboard_stocks+=1; 
             else:
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.poor_keyboard_worth+=price_float
                   y.poor_keyboard_stocks+=1; 
         y.save()
         order.save()
      if product_type=="mouse":
         order = mouse.objects.get(id=orderid)
         order.status = update
         if update!="Completed" : order.expected_date = datetime.now() + timedelta(days=4)
         else:
             if condition=="good":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.good_mouse_worth+=price_float
                   y.good_mouse_stocks+=1; 
             elif condition=="best":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.best_mouse_worth+=price_float
                   y.best_mouse_stocks+=1; 
             else: 
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.poor_mouse_worth+=price_float
                   y.poor_mouse_stocks+=1; 
         y.save()
         order.save()
      if product_type=="speaker":
         order = speakers.objects.get(id=orderid)
         order.status = update
         if update!="Completed" : order.expected_date = datetime.now() + timedelta(days=4)
         else:
             if condition=="good":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.good_speaker_worth+=price_float
                   y.good_speaker_stocks+=1; 
             elif condition=="best":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.best_speaker_worth+=price_float
                   y.best_speaker_stocks+=1; 
             else:
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.poor_speaker_worth+=price_float
                   y.poor_speaker_stocks+=1; 
         y.save()
         order.save()
      if product_type=="tv":
         order = tvs.objects.get(id=orderid)
         order.status = update
         if update!="Completed" : order.expected_date = datetime.now() + timedelta(days=4)
         else:
             if condition=="good":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.good_tv_worth+=price_float
                   y.good_tv_stocks+=1; 
             elif condition=="best":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.best_tv_worth+=price_float
                   y.best_tv_stocks+=1; 
             else:
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.poor_tv_worth+=price_float
                   y.poor_tv_stocks+=1; 
         y.save()
         order.save()
      if product_type=="watch":
         order = watches.objects.get(id=orderid)
         order.status = update
         if update!="Completed" : order.expected_date = datetime.now() + timedelta(days=4)
         else:
             if condition=="good":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.good_watch_worth+=price_float
                   y.good_watch_stocks+=1; 
             if condition=="best":
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.best_watch_worth+=price_float
                   y.best_watch_stocks+=1; 
             else:
                   price_str = price[:-3] + '.00'  # Append ".00" to the string to create a valid float value
                   price_float = float(price_str)
                   y.poor_watch_worth+=price_float
                   y.poor_watch_stocks+=1; 
         y.save()
         order.save()
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
   y = VendorStocks.objects.all()
   return render(request,'orghome.html',{'y':y})

def SellerOrderPage(request):
     if request.method=='POST':
        
        orderid=request.POST.get('order');
        product_type=request.POST.get('product');
        
        if product_type=="headphone":
         order = Headphones.objects.get(id=orderid)
         order.delete()
        if product_type=="phone":
         order = phones.objects.get(id=orderid)
         order.delete()
        if product_type=="mouse":
         order = mouse.objects.get(id=orderid)
         order.delete()
        if product_type=="keyboard":
         order = Keyboards.objects.get(id=orderid)
         order.delete()
        if product_type=="speaker":
         order = speakers.objects.get(id=orderid)
         order.delete()
        if product_type=="tve":
         order = tvs.objects.get(id=orderid)
         order.delete()
        if product_type=="watch":
         order = watches.objects.get(id=orderid)
         order.delete()
        if product_type=="laptop":
         order = laptops.objects.get(id=orderid)
         order.delete()
    
     headphone=Headphones.objects.all().filter(userid=request.user)
     phone=phones.objects.all().filter(userid=request.user)
     tv=tvs.objects.all().filter(userid=request.user)
     speaker=speakers.objects.all().filter(userid=request.user)
     watch=watches.objects.all().filter(userid=request.user)
     keyboard=Keyboards.objects.all().filter(userid=request.user)
     m=mouse.objects.all().filter(userid=request.user)
     laptop=laptops.objects.all().filter(userid=request.user)
     return render (request,'sellerorder.html',{'headphone':headphone,'phone':phone,'tv':tv,'speaker':speaker,'watch':watch,'keyboard':keyboard,'mouse':m,'laptop':laptop})
     
    
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


def VendorOrderPage(request):
    y=VendorStocks.objects.filter(vendor_id=request.user)

    return render (request,'vendororder.html',{'y':y})