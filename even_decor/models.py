from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Decor_DB(models.Model):
    Username=models.CharField(max_length=20,unique=True)
    Number=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Businessname=models.CharField(max_length=20,unique=True)
    Place=models.CharField(max_length=50)

    Password=models.CharField(max_length=15)
    Image=models.ImageField(upload_to='img',default="default.jpg")
    Experience=models.IntegerField(default=2)



    def __str__(self):
        return self.Username 



class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    DID=models.ForeignKey(Decor_DB,on_delete=models.CASCADE,default='1')

    def save(self):
        self.slug=slugify(self.name)
        super(Category,self).save()  

    def __str__(self):
        return self.name

class Product(models.Model):
    Name=models.CharField(max_length=20,unique=True)
    Desc=models.CharField(max_length=500)
    Price=models.CharField(max_length=50)
    DecorID=models.ForeignKey(Decor_DB,on_delete=models.CASCADE,default='1')
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default='1')
    Image=models.ImageField(upload_to='decor')
    Book=models.BooleanField(default="False")
    userid=models.CharField(max_length=50,default="0")
    rate=models.CharField(max_length=20,default="0")


    def __str__(self):
        return self.Name 
    
class D_image(models.Model):
    ProductID=models.ForeignKey(Product,on_delete=models.CASCADE,default='1')
    Image=models.ImageField(upload_to='decor')
    

class book(models.Model):
    username=models.CharField(max_length=20)
    number=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    prodid=models.CharField(max_length=20,default="0")
    Decorid=models.CharField(max_length=20,default="0")
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
    
class drate(models.Model):
    Username=models.CharField(max_length=20,unique=True)
    Number=models.CharField(max_length=50)
    userid=models.CharField(max_length=20,default="0")
    prodid=models.CharField(max_length=20,default="0")
    Decorid=models.CharField(max_length=20,default="0") 
    Email=models.EmailField(max_length=50)
    
    def __str__(self):
        return self.Username
    