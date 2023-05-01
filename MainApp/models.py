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