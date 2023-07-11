from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from event_user.models import *
# from . forms import *
import os
# Create your views here.
def C_home(request):
    
    return render(request,'Cater/index.html')

def C_register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        number=request.POST.get("number")
        place=request.POST.get("place")
        email=request.POST.get("email")
        Exp=request.POST.get("experience")

        Bname=request.POST.get('bname')
        img=request.FILES.get('img')

        p1=request.POST.get("password")
        p2=request.POST.get("confirmpassword")
        

        
   
        if p1==p2:
            if Cater_DB.objects.filter(Username=username).exists():
                messages.info(request,'Username Already Exists')
            else: 
              userdata=Cater_DB(Username=username,Number=number,Place=place,Image=img,Email=email,Experience=Exp,Businessname=Bname,Password=p1)
              userdata.save()
              return redirect("clog")          
        else:  
             messages.info(request,'password not match')

    return render(request,'Cater/Register.html')
    

def C_login(request):
    if request.method=="POST":
        try:
            username=request.POST.get("username")
            password=request.POST.get("password")
            log=Cater_DB.objects.get(Username=username,Password=password)
            request.session['Username']=log.Username
            request.session['id']=log.id

            return redirect('chome')
        except Cater_DB.DoesNotExist as e :
            messages.info(request,'Invalid User')
    return render(request,'Cater/login.html')

# def C_Addcateg(request):
#     if request.method=="POST":
#        cname=request.POST.get("cname")
#        cid=request.POST['cid']
#        categsave=F_Category(name=cname,CID_id=cid)
#        categsave=F_Category(name=cname)
#        categsave.save()
#        return redirect("chome")
#     return render(request,'Cater/Addcateg.html')
def C_Addpro(request):
    if request.method=='POST':
       name=request.POST.get("name")
       descrption=request.POST.get("Desc")
       price=request.POST.get("Price")
       img=request.FILES.get('img')
       Images=request.FILES.getlist('image')
       
       for f in Images:
           file=F_image(Image=f)
           file.save()
    #     return HttpResponse('Images added successfully')
    #    
    #    cid=request.POST['cid']
    #    did=request.POST['did']
       addsave=F_Product(Name=name,Desc=descrption,Price=price,Image=img)
       addsave.save()
       return redirect("chome")
    # categid=F_Category.objects.all() 
    return render(request,'Cater/Addproduct.html')

from django.http import HttpResponse

def addimg(request,cid):
    if request.method=='POST':
        Images=request.FILES.getlist('image')
        for f in Images:
            file=F_image(Image=f,ProductID_id=cid)
            file.save()
        return redirect('chome')
    return render(request,'Cater/addimage.html')


def C_dashboard(request):
    hid=request.session['id']

    prof=Cater_DB.objects.get(id=hid)
    return render(request,'Cater/dashboard.html', {'pro':prof})

def C_editpro(request,id):
    edit=Cater_DB.objects.get(id=id)
    if request.method=="POST":
        
        if len(request.FILES)!=0:
    #         if len(edit.Image)>0:
    #             os.remove(edit.Image.path)
            edit.Image=request.FILES.get('img')

        edit.Username=request.POST.get("username")
        edit.Number=request.POST.get("number")
        edit.Place=request.POST.get("place")
        edit.Email=request.POST.get("email")
        edit.Experience=request.POST.get("experience")

        edit.Businessname=request.POST.get('bname')
        
        edit.Password=request.POST.get("password")
        edit.save()
        # Decor_DB.objects.filter(id=id).update(Username=username,Number=number,Place=place,Image=img,Email=email,Experience=Exp,Businessname=Bname,Password=p1)
        
        return redirect("Cdashboard")
    return render(request,'Cater/editprofile.html',{'pro':edit})


def C_Viewpagedecor(request):
    proview=F_Product.objects.all()
    return render(request,'Cater/Viewpage.html',{'proview':proview})

def C_proDview(request,tid): 
    Dview=F_Product.objects.get(id=tid)
    return render(request,'Cater/viewdetail.html',{'proview':Dview})

def C_produpdate(request,id):
    prod=F_Product.objects.get(id=id)
    if request.method=="POST":
       
        
        if len(request.FILES)!=0:
    #         if len(edit.Image)>0:
    #             os.remove(edit.Image.path)
            prod.Image=request.FILES.get('img')

        # Images=request.FILES.getlist('image')
        # for f in Images:
        #     file=F_image(Image=f,ProductID_id=id)
        #     file.save()
        prod.Name=request.POST.get("name")
        prod.Desc=request.POST.get("Desc")
        prod.Price=request.POST.get("Price")
       
        prod.save()
        # Decor_DB.objects.filter(id=id).update(Username=username,Number=number,Place=place,Image=img,Email=email,Experience=Exp,Businessname=Bname,Password=p1)
        
        return redirect("CViewpage")
    return render(request,'Cater/editproduct.html',{'prod':prod})
    

def C_proddelete(request,pid):
    prod = F_Product.objects.get(id=pid)
    if request.method == "POST":
        prod.delete()
        # pro=Product.objects.all()
        return redirect("CViewpage")
    return render(request,'Cater/proddelete.html',{'prod':prod})

def C_bookdetails(request):
    cid=request.session['Username']
    cdata=C_book.objects.filter(caterid=cid)
    return render(request,'Cater/bookdetails.html',{'cdata':cdata})


def C_customerdetails(request,cid): 
    cdata=User_DB.objects.get(id=cid)
    return render(request,'Cater/customerdetails.html',{'data':cdata})

def C_productdetails(request,pid): 
    data=F_Product.objects.get(id=pid)
    return render(request,'Cater/productdetails.html',{'data':data})

def C_accept(request,sid): 
    C_book.objects.filter(id=sid).update(accept=True)
    C_book.objects.filter(id=sid).update(reject=False)

    # uid=request.session['id']
    # ddata=Product.objects.get(id=did)
    # ddata.userid=uid
    # ddata.save()+
    
    return redirect('cbdetails')

def C_reject(request,sid): 
    C_book.objects.filter(id=sid).update(reject=True)
    C_book.objects.filter(id=sid).update(accept=False)
    
    return redirect('cbdetails')

