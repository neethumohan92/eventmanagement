from django.db import models
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Admin_DB(models.Model):
    Username=models.CharField(max_length=20,unique=True)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=15)
    def __str__(self):
        return self.Username