from django.db import models

# Create your models here.
class UserDetails(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    pin = models.IntegerField()
    phone = models.IntegerField()
   
    def __str__(self):
        return self.email

class Headphones(models.Model):
    id=models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    userpin = models.IntegerField()
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    model_no = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    overall_condition = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='headphones/')
    order_date = models.DateTimeField()
    expected_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id} -    {self.userid}  - {self.company_name}  - {self.model_no} - {self.status}"

class Keyboards(models.Model):
    id=models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    userpin = models.IntegerField()
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    model_no = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    overall_condition = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='keyboards/')
    order_date = models.DateTimeField()
    expected_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=50)
  
    
    def __str__(self):
        return f"{self.id} -     {self.userid} - {self.company_name} - {self.model_no}- {self.status}"

class laptops(models.Model):
    id=models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    userpin = models.IntegerField()
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    model_no = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    overall_condition = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='laptops/')
    order_date = models.DateTimeField()
    expected_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=50)
  
    
    def __str__(self):
        return f"{self.id} -     {self.userid} - {self.company_name} - {self.model_no}- {self.status}"

class mouse(models.Model):
    id=models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    userpin = models.IntegerField()
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    model_no = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    overall_condition = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='mouse/')
    order_date = models.DateTimeField()
    expected_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=50)
  
    
    def __str__(self):
        return f"{self.id} -    {self.userid} - {self.company_name} - {self.model_no}- {self.status}"

class phones(models.Model):
    id=models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    userpin = models.IntegerField()
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    model_no = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    order_date = models.DateTimeField()
    expected_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=50)
    overall_condition = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='phones/')
  
    
    def __str__(self):
        return f"{self.id} -    {self.userid} - {self.company_name} - {self.model_no}- {self.status}"
class speakers(models.Model):
    id=models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    userpin = models.IntegerField()
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    model_no = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    overall_condition = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='speakers/')
    order_date = models.DateTimeField()
    expected_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=50)
  
    
    def __str__(self):
        return f"{self.id} -     {self.userid} - {self.company_name} - {self.model_no}- {self.status}"

class tvs(models.Model):
    id=models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    userpin = models.IntegerField()
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    model_no = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    overall_condition = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='tvs/')
    order_date = models.DateTimeField()
    expected_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=50)
  
    
    def __str__(self):
        return f"{self.id} -     {self.userid} - {self.company_name} - {self.model_no}- {self.status}"

class watches(models.Model):
    id=models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)
    userpin = models.IntegerField()
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    model_no = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    overall_condition = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='watches/')
    order_date = models.DateTimeField()
    expected_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=50)
  
    
    def __str__(self):
        return f"{self.id} -    {self.userid} - {self.company_name} - {self.model_no}- {self.status}"




class VendorStocks(models.Model):
    id = models.AutoField(primary_key=True)
    vendor_id = models.CharField(max_length=50)
    pin = models.IntegerField()
    phone = models.IntegerField()
    good_headphone_stocks = models.IntegerField(default=0)
    best_headphone_stocks = models.IntegerField(default=0)
    poor_headphone_stocks = models.IntegerField(default=0)
    good_headphone_worth = models.BigIntegerField(default=0)
    best_headphone_worth = models.BigIntegerField(default=0)
    poor_headphone_worth = models.BigIntegerField(default=0)
    good_speaker_stocks = models.IntegerField(default=0)
    best_speaker_stocks = models.IntegerField(default=0)
    poor_speaker_stocks = models.IntegerField(default=0)
    good_speaker_worth = models.BigIntegerField(default=0)
    best_speaker_worth = models.BigIntegerField(default=0)
    poor_speaker_worth = models.BigIntegerField(default=0)
    good_tv_stocks = models.IntegerField(default=0)
    best_tv_stocks = models.IntegerField(default=0)
    poor_tv_stocks = models.IntegerField(default=0)
    good_tv_worth = models.BigIntegerField(default=0)
    best_tv_worth = models.BigIntegerField(default=0)
    poor_tv_worth = models.BigIntegerField(default=0)
    good_laptop_stocks = models.IntegerField(default=0)
    best_laptop_stocks = models.IntegerField(default=0)
    poor_laptop_stocks = models.IntegerField(default=0)
    good_laptop_worth = models.BigIntegerField(default=0)
    best_laptop_worth = models.BigIntegerField(default=0)
    poor_laptop_worth = models.BigIntegerField(default=0)
    good_keyboard_stocks = models.IntegerField(default=0)
    best_keyboard_stocks = models.IntegerField(default=0)
    poor_keyboard_stocks = models.IntegerField(default=0)
    good_keyboard_worth = models.BigIntegerField(default=0)
    best_keyboard_worth = models.BigIntegerField(default=0)
    poor_keyboard_worth = models.BigIntegerField(default=0)
    good_mouse_stocks = models.IntegerField(default=0)
    best_mouse_stocks = models.IntegerField(default=0)
    poor_mouse_stocks = models.IntegerField(default=0)
    good_mouse_worth = models.BigIntegerField(default=0)
    best_mouse_worth = models.BigIntegerField(default=0)
    poor_mouse_worth = models.BigIntegerField(default=0)
    good_phone_stocks = models.IntegerField(default=0)
    best_phone_stocks = models.IntegerField(default=0)
    poor_phone_stocks = models.IntegerField(default=0)
    good_phone_worth = models.BigIntegerField(default=0)
    best_phone_worth = models.BigIntegerField(default=0)
    poor_phone_worth = models.BigIntegerField(default=0)
    good_watch_stocks = models.IntegerField(default=0)
    best_watch_stocks = models.IntegerField(default=0)
    poor_watch_stocks = models.IntegerField(default=0)
    good_watch_worth = models.BigIntegerField(default=0)
    best_watch_worth = models.BigIntegerField(default=0)
    poor_watch_worth = models.BigIntegerField(default=0)

    def __str__(self):
        return self.vendor_id
