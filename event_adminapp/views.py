from django.shortcuts import render,redirect
from django.contrib import messages
from even_decor.models import *
from event_photography.models import *
from event_user.models import *
from event_cater.models import *
from event_spot.models import *
from .models import *

# Create your views here.

def A_home(request):
    scount=S_book.objects.all()
    ccount=C_book.objects.all()
    dcount=book.objects.all()
    pcount=P_book.objects.all()
    
    
    return render(request,'EAdmin/index.html',{'scount':scount,'ccount':ccount,'dcount':dcount,'pcount':pcount,})

def A_register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        
        p1=request.POST.get("password")
        p2=request.POST.get("confirmpassword")
   
        if p1==p2:
            if Admin_DB.objects.filter(Email=email).exists():
                messages.info(request,'Email Already Exists')
            else: 
              userdata=Admin_DB(Username=username,Email=email,Password=p1)
              userdata.save()
              return redirect("alog")          
        else:  
             messages.info(request,'password not match')
    return render(request,'EAdmin/Register.html')

def A_login(request):
    if request.method=="POST":
        try:
            messages.info(request,'Invalid User')
            
            email=request.POST.get("email")
            password=request.POST.get("password")
            log=Admin_DB.objects.get(Email=email,Password=password)
            request.session['Username']=log.Username
            request.session['id']=log.id

            return redirect('ahome')
        except Admin_DB.DoesNotExist as e :
            messages.info(request,'Invalid User')
    return render(request,'EAdmin/login.html')

def table(request):
    uid=request.session['id']
    udata=User_DB.objects.all()
    ddata=Decor_DB.objects.all()
    cdata=Cater_DB.objects.all()
    
    sdata=spot_db.objects.all()
    pdata=Photo_DB.objects.all()


    return render(request,'EAdmin/table.html',{'ddata':ddata, 'sdata':sdata, 'cdata':cdata, 'pdata':pdata,'udata':udata})

# def table(request):
#     uid=request.session['id']
    
#     ddata=book.objects.all()
#     cdata=Cater_DB.objects.all()
#     sdata=spot_db.objects.all()
#     pdata=Photo_DB.objects.all()

#     return render(request,'EAdmin/table.html',{'ddata':ddata, 'sdata':sdata, 'cdata':cdata, 'pdata':pdata})z3     


