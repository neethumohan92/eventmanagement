from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from event_user.models import *
import os
# Create your views here.
def s_home(request):
    
    return render(request,'Spot/index.html')

def s_register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        number=request.POST.get("number")
        place=request.POST.get("place")
        email=request.POST.get("email")
        Exp=request.POST.get("experience")
        loc=request.POST.get("location")
        Bname=request.POST.get('bname')
        img=request.FILES.get('img')

        p1=request.POST.get("password")
        p2=request.POST.get("confirmpassword")
        

        
   
        if p1==p2:
            if spot_db.objects.filter(Username=username).exists():
                messages.info(request,'Username Already Exists')
            else: 
              userdata=spot_db(Username=username,Number=number,Place=place,Image=img,Email=email,Experience=Exp,Businessname=Bname,Password=p1,Location=loc)
              userdata.save()
              return redirect("slog")          
        else:  
             messages.info(request,'password not match')

    return render(request,'Spot/Register.html')
    

def S_login(request):
    if request.method=="POST":
        try:
            username=request.POST.get("username")
            password=request.POST.get("password")
            log=spot_db.objects.get(Username=username,Password=password)
            request.session['Username']=log.Username
            request.session['id']=log.id

            return redirect('shome')
        except spot_db.DoesNotExist as e :
            messages.info(request,'Invalid User')
    return render(request,'Spot/login.html')

# def P_Addcateg(request):
#     if request.method=="POST":
#        cname=request.POST.get("cname")
#        categsave=P_Category(name=cname)
#        categsave.save()
#        return redirect("phome")
#     return render(request,'Photography/Addcateg.html')

def S_Addpro(request):
    if request.method=='POST':
       name=request.POST.get("name")
       descrption=request.POST.get("Desc")
       price=request.POST.get("Price")
       
       img=request.FILES.get('img')
       cid=request.POST['cid']
    #    did=request.POST['did']
       addsave=s_product(Name=name,Desc=descrption,Price=price,Image=img,SpotID_id=cid)
       addsave.save()
       return redirect("shome")
    # categid=P_Category.objects.all() 
    return render(request,'Spot/Addproduct.html')


# def Viewpagedecor(request,pk):
#     proview=Product.objects.filter(DecorID=pk)
#     return render(request,'Decor/Viewpage.html',{'proview':proview})


def S_dashboard(request):
    hid=request.session['id']

    prof=spot_db.objects.get(id=hid)
    return render(request,'Spot/dashboard.html', {'pro':prof})

def S_editpro(request,id):
    edit=spot_db.objects.get(id=id)
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
        edit.Location=request.POST.get("location")

        edit.Businessname=request.POST.get('bname')
        
        edit.Password=request.POST.get("password")
        edit.save()
        # Decor_DB.objects.filter(id=id).update(Username=username,Number=number,Place=place,Image=img,Email=email,Experience=Exp,Businessname=Bname,Password=p1)
        
        return redirect("Sdashboard")
    return render(request,'Spot/editprofile.html',{'pro':edit})


def S_Viewpagedecor(request):
    proview=s_product.objects.all()
    return render(request,'Spot/Viewpage.html',{'proview':proview})

def S_proDview(request,tid): 
    Dview=s_product.objects.get(id=tid)
    return render(request,'Spot/viewdetail.html',{'proview':Dview})

def S_produpdate(request,id):
    prod=s_product.objects.get(id=id)
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
        
        return redirect("SViewpage")
    return render(request,'Spot/editproduct.html',{'prod':prod})
    

def S_proddelete(request,pid):
    prod = s_product.objects.get(id=pid)
    if request.method == "POST":
        prod.delete()
        # pro=Product.objects.all()
        return redirect("SViewpage")
    return render(request,'Spot/proddelete.html',{'prod':prod})



def S_bookdetails(request):
    sid=request.session['Username']
    sdata=S_book.objects.filter(Spotid=sid)
    return render(request,'Spot/bookdetails.html',{'sdata':sdata,'sid':sid})

def S_customerdetails(request,cid): 
    cdata=User_DB.objects.get(id=cid)
    return render(request,'Spot/customerdetails.html',{'data':cdata})

def S_productdetails(request,pid): 
    data=s_product.objects.get(id=pid)
    return render(request,'Spot/productdetails.html',{'data':data})

def S_accept(request,sid): 
    S_book.objects.filter(id=sid).update(accept=True)
    S_book.objects.filter(id=sid).update(reject=False)
    
    # uid=request.session['id']
    # ddata=Product.objects.get(id=did)
    # ddata.userid=uid
    # ddata.save()
    return redirect('sbdetails')

def S_reject(request,sid): 
    S_book.objects.filter(id=sid).update(reject=True)
    S_book.objects.filter(id=sid).update(accept=False)
    
    return redirect('sbdetails')

def addimg(request,cid):
    if request.method=='POST':
        Images=request.FILES.getlist('image')
        for f in Images:
            file=S_image(Image=f,ProductID_id=cid)
            file.save()
        return redirect('shome')
    return render(request,'Spot/addimage.html')