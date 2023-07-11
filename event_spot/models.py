from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class spot_db(models.Model):
    Username=models.CharField(max_length=20)
    Number=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Businessname=models.CharField(max_length=20)
    Place=models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
    Password=models.CharField(max_length=15)
    Image=models.ImageField(upload_to='Spot')
    Experience=models.IntegerField(default=2)



    def __str__(self):
        return self.Username 

class s_product(models.Model):
    Name=models.CharField(max_length=20)
    Desc=models.CharField(max_length=500)
    Price=models.CharField(max_length=50)
    SpotID=models.ForeignKey(spot_db,on_delete=models.CASCADE,default='1')
    # FCategory=models.ForeignKey(P_Category,on_delete=models.CASCADE,default='1')
    Image=models.ImageField(upload_to='cater')
    Book=models.BooleanField(default="False")
    
    userid=models.CharField(max_length=20,default="0")
    rate=models.CharField(max_length=20,default="0")
    


    def __str__(self):
        return self.Name 
    
class S_image(models.Model):
    ProductID=models.ForeignKey(s_product,on_delete=models.CASCADE,default='1')
    Image=models.ImageField(upload_to='cater')
    
    
class S_book(models.Model):
    username=models.CharField(max_length=20)
    number=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    prodid=models.CharField(max_length=20,default="0")
    Spotid=models.CharField(max_length=20,default="0")
    userid=models.CharField(max_length=20,default="0")
    price=models.CharField(max_length=20,default="0")
    book=models.BooleanField(default="False")
    status=models.CharField(max_length=20,default="Pending")
    accept=models.BooleanField(default="False")
    reject=models.BooleanField(default="False")
    rate=models.CharField(max_length=20,default="0")
    review=models.CharField(max_length=20,default="Null")
    paystatus=models.BooleanField(default="False")
    
    

    def __str__(self):
        return self.username 
    
class srate(models.Model):
    Username=models.CharField(max_length=20,unique=True)
    Number=models.CharField(max_length=50)
    userid=models.CharField(max_length=20,default="0")
    prodid=models.CharField(max_length=20,default="0")
    Spotid=models.CharField(max_length=20,default="0") 
    Email=models.EmailField(max_length=50)
    
    def __str__(self):
        return self.Username