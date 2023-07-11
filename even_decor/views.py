from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from . forms import *
from event_user.models import *
import os
# Create your views here.
def D_home(request):
    
    return render(request,'Decor/index.html')

def D_register(request):
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
            if Decor_DB.objects.filter(Username=username).exists():
                messages.info(request,'Username Already Exists')
            else: 
              userdata=Decor_DB(Username=username,Number=number,Place=place,Image=img,Email=email,Experience=Exp,Businessname=Bname,Password=p1)
              userdata.save()
              return redirect("dlog")          
        else:  
             messages.info(request,'password not match')

    return render(request,'Decor/Register.html')
    

def D_login(request):
    if request.method=="POST":
        try:
            username=request.POST.get("username")
            password=request.POST.get("password")
            log=Decor_DB.objects.get(Username=username,Password=password)
            request.session['Username']=log.Username
            request.session['id']=log.id

            return redirect('dhome')
        except Decor_DB.DoesNotExist as e :
            messages.info(request,'Invalid User')
    return render(request,'Decor/login.html')

def Addcateg(request):
    if request.method=="POST":
       cname=request.POST.get("cname")
       did=request.POST['did']
       categsave=Category(name=cname,DID_id=did)
       categsave.save()
       return redirect("dhome")
    return render(request,'Decor/Addcateg.html')

def Addpro(request):
    Did=request.session['id']
    categid=Category.objects.filter(DID=Did) 
    if request.method=='POST':
       name=request.POST.get("name")
       descrption=request.POST.get("Desc")
       price=request.POST.get("Price")
       
       img=request.FILES.get('img')
       cid=request.POST['cid']
       did=request.POST['did']
       addsave=Product(Name=name,Desc=descrption,Price=price,Image=img,Category_id=cid,DecorID_id=did)
       addsave.save()
       return redirect("dhome")
    
    return render(request,'Decor/Addproduct.html',{'cid':categid})

def dashboard(request):
    hid=request.session['id']

    prof=Decor_DB.objects.get(id=hid)
    return render(request,'Decor/dashboard.html', {'pro':prof})

def editpro(request,id):
    edit=Decor_DB.objects.get(id=id)
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
        
        return redirect("dashboard")
    return render(request,'Decor/editprofile.html',{'pro':edit})


def Viewpagedecor(request):
    proview=Product.objects.all()
    return render(request,'Decor/Viewpage.html',{'proview':proview})

def proDview(request,tid): 
    Dview=Product.objects.get(id=tid)
    return render(request,'Decor/viewdetail.html',{'proview':Dview})

def produpdate(request,id):
    prod=Product.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
    #         if len(edit.Image)>0:
    #             os.remove(edit.Image.path)
            prod.Image=request.FILES.get('img')

        prod.Name=request.POST.get("name")
        prod.Desc=request.POST.get("Desc")
        prod.Price=request.POST.get("Price")
       
        prod.save()
        # Decor_DB.objects.filter(id=id).update(Username=username,Number=number,Place=place,Image=img,Email=email,Experience=Exp,Businessname=Bname,Password=p1)
        
        return redirect("Viewpage")
    return render(request,'Decor/editproduct.html',{'prod':prod})
    

def proddelete(request,pid):
    prod = Product.objects.get(id=pid)
    if request.method == "POST":
        prod.delete()
        # pro=Product.objects.all()
        return redirect("Viewpage")
    return render(request,'Decor/proddelete.html',{'prod':prod})


def bookdetails(request):
    did=request.session['Username']
    ddata=book.objects.filter(Decorid=did)
    
    return render(request,'Decor/bookdetails.html',{'ddata':ddata})

def customerdetails(request,did): 
    cdata=User_DB.objects.get(id=did)
    return render(request,'Decor/customerdetails.html',{'data':cdata})

def productdetails(request,pid): 
    data=Product.objects.get(id=pid)
    return render(request,'Decor/productdetails.html',{'data':data})

def D_accept(request,sid): 
    book.objects.filter(id=sid).update(accept=True)
    book.objects.filter(id=sid).update(reject=False)
    
    # uid=request.session['id']
    # ddata=Product.objects.get(id=did)
    # ddata.userid=uid
    # ddata.save()
    return redirect('bdetails')

def D_reject(request,sid): 
    book.objects.filter(id=sid).update(reject=True)
    book.objects.filter(id=sid).update(accept=False)
    
    return redirect('bdetails')

def addimg(request,did):
    if request.method=='POST':
        Images=request.FILES.getlist('image')
        for f in Images:
            file=D_image(Image=f,ProductID_id=did)
            file.save()
        return redirect('dhome')
    return render(request,'Decor/addimage.html')