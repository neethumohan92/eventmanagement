from django.db import models

# Create your models here.
class User_DB(models.Model):
    Username=models.CharField(max_length=20,unique=True)
    Number=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=15)
    Image=models.ImageField(upload_to='img')
    Date=models.DateField(null=True)
    Function=models.CharField(max_length=50)
    C_Accept=models.BooleanField(default="False")

    C_Reject=models.BooleanField(default="False")
    S_Accept=models.BooleanField(default="False")

    S_Reject=models.BooleanField(default="False")
    D_Accept=models.BooleanField(default="False")

    D_Reject=models.BooleanField(default="False")
    P_Accept=models.BooleanField(default="False")

    P_Reject=models.BooleanField(default="False")



    def __str__(self):
        return self.Username
    
