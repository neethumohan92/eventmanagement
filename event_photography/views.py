from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from event_user.models import *
# from . forms import *
import os
# Create your views here.
def P_home(request):
    
    return render(request,'Photography/index.html')

def P_register(request):
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
            if Photo_DB.objects.filter(Username=username).exists():
                messages.info(request,'Username Already Exists')
            else: 
              userdata=Photo_DB(Username=username,Number=number,Place=place,Image=img,Email=email,Experience=Exp,Businessname=Bname,Password=p1)
              userdata.save()
              return redirect("plog")          
        else:  
             messages.info(request,'password not match')

    return render(request,'Photography/Register.html')
    

def P_login(request):
    if request.method=="POST":
        try:
            username=request.POST.get("username")
            password=request.POST.get("password")
            log=Photo_DB.objects.get(Username=username,Password=password)
            request.session['Username']=log.Username
            request.session['id']=log.id

            return redirect('phome')
        except Photo_DB.DoesNotExist as e :
            messages.info(request,'Invalid User')
    return render(request,'Photography/login.html')

def P_Addcateg(request):
    if request.method=="POST":
       cname=request.POST.get("cname")
       pid=request.POST['pid']
       categsave=P_Category(name=cname,PID_id=pid)
       categsave.save()
       return redirect("phome")
    return render(request,'Photography/Addcateg.html')

def P_Addpro(request):
    Pid=request.session['id']
    categid=P_Category.objects.filter(PID=Pid) 
    if request.method=='POST':
       name=request.POST.get("name")
       descrption=request.POST.get("Desc")
       price=request.POST.get("Price")
       
       img=request.FILES.get('img')
       cid=request.POST['cid']
       did=request.POST['did']
       addsave=P_Product(Name=name,Desc=descrption,Price=price,Image=img,FCategory_id=cid,CaterID_id=did)
       addsave.save()
       return redirect("phome")
    categid=P_Category.objects.all() 
    return render(request,'Photography/Addproduct.html',{'cid':categid})


# def Viewpagedecor(request,pk):
#     proview=Product.objects.filter(DecorID=pk)
#     return render(request,'Decor/Viewpage.html',{'proview':proview})


def P_dashboard(request):
    hid=request.session['id']

    prof=Photo_DB.objects.get(id=hid)
    return render(request,'Photography/dashboard.html', {'pro':prof})

def P_editpro(request,id):
    edit=Photo_DB.objects.get(id=id)
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
        
        return redirect("Pdashboard")
    return render(request,'Photography/editprofile.html',{'pro':edit})


def P_Viewpagedecor(request):
    proview=P_Product.objects.all()
    return render(request,'Photography/Viewpage.html',{'proview':proview})

def P_proDview(request,tid): 
    Dview=P_Product.objects.get(id=tid)
    return render(request,'Photography/viewdetail.html',{'proview':Dview})

def P_produpdate(request,id):
    prod=P_Product.objects.get(id=id)
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
        
        return redirect("PViewpage")
    return render(request,'Photography/editproduct.html',{'prod':prod})
    

def P_proddelete(request,pid):
    prod = P_Product.objects.get(id=pid)
    if request.method == "POST":
        prod.delete()
        # pro=Product.objects.all()
        return redirect("PViewpage")
    return render(request,'Photography/proddelete.html',{'prod':prod})


def P_bookdetails(request):
    sid=request.session['Username']
    pdata=P_book.objects.filter(photoid=sid)

    return render(request,'Photography/bookdetails.html',{'pdata':pdata})

def P_customerdetails(request,cid): 
    cdata=User_DB.objects.get(id=cid)
    return render(request,'Photography/customerdetails.html',{'data':cdata})

def P_productdetails(request,pid): 
    data=P_Product.objects.get(id=pid)
    return render(request,'Photography/productdetails.html',{'data':data})

def P_accept(request,sid): 
    P_book.objects.filter(id=sid).update(accept=True)
    P_book.objects.filter(id=sid).update(reject=False)
    
    # uid=request.session['id']
    # ddata=Product.objects.get(id=did)
    # ddata.userid=uid
    # ddata.save()
    return redirect('pbdetails')

def P_reject(request,sid): 
    P_book.objects.filter(id=sid).update(reject=True)
    P_book.objects.filter(id=sid).update(accept=False)
    
    return redirect('pbdetails')

def addimg(request,cid):
    if request.method=='POST':
        Images=request.FILES.getlist('image')
        for f in Images:
            file=P_image(Image=f,ProductID_id=cid)
            file.save()
        return redirect('phome')
    return render(request,'Photography/addimage.html')