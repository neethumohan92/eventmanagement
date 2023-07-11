from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from even_decor.models import *
from event_photography.models import *
from event_cater.models import *
from event_spot.models import *
import razorpay
from Event_Management.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY

# Create your views here.
def uhome(request):
    return render(request,'User/index.html')

def uregister(request):
    if request.method=="POST":
        username=request.POST.get("username")
        number=request.POST.get("number")
        gender=request.POST.get("gender")
        email=request.POST.get("email")
        function=request.POST.get("function")
        date=request.POST.get('date')

        p1=request.POST.get("password")
        p2=request.POST.get("confirmpassword")
   
        if p1==p2:
            if User_DB.objects.filter(Email=email).exists():
                messages.info(request,'Email Already Exists')
            else: 
              userdata=User_DB(Username=username,Number=number,Gender=gender,Email=email,Function=function,Date=date,Password=p1)
              userdata.save()
              return redirect("ulog")          
        else:  
             messages.info(request,'password not match')

    return render(request,'User/Register.html')
    

def ulogin(request):
    if request.method =="POST":
        try:
            username=request.POST.get("username")
            password=request.POST.get("password")
            log=User_DB.objects.get(Username=username,Password=password)
            request.session['Username']=log.Username
            request.session['id']=log.id

            return redirect('uhome')
        except User_DB.DoesNotExist as e :
            messages.info(request,'Invalid User')
    return render(request,'User/login.html')


def Dashboard(request):
    hid=request.session['id']

    prof=User_DB.objects.get(id=hid)
    return render(request,'User/dashboard.html', {'pro':prof})

def Editpro(request,uid):
    edit=User_DB.objects.get(id=uid)
    if request.method=="POST":

        edit.Username=request.POST.get("username")
        edit.Number=request.POST.get("number")
        edit.Email=request.POST.get("email")
        
        if len(request.POST.get("date"))!=0:
            edit.Date=request.POST.get("date")

        edit.Function=request.POST.get("function")
        edit.Password=request.POST.get("password")
        edit.save()
        # Decor_DB.objects.filter(id=id).update(Username=username,Number=number,Place=place,Image=img,Email=email,Experience=Exp,Businessname=Bname,Password=p1)
        
        return redirect("dashboard")
    return render(request,'User/editprofile.html',{'pro':edit})


def Decorations(request):
    proview=Product.objects.all()
    return render(request,'User/Decorations.html',{'proview':proview})

def Locations(request):
    proview=s_product.objects.all()
    return render(request,'User/spot.html',{'proview':proview})

def Caterings(request):
    proview=F_Product.objects.all()
    return render(request,'User/catering.html',{'proview':proview})

def Photography(request):
    proview=P_Product.objects.all()
    return render(request,'User/Photography.html',{'proview':proview})

def Dview(request,did): 
    Dview=Product.objects.get(id=did)
    de_id=Dview.DecorID
    Decor=Decor_DB.objects.get(Username=de_id)
    return render(request,'User/decorview.html',{'proview':Dview,'decor':Decor})

def Pview(request,pid): 
    Pview=P_Product.objects.get(id=pid)
    ph_id=Pview.CaterID
    Photo=Photo_DB.objects.get(Username=ph_id)
    return render(request,'User/photoview.html',{'proview':Pview,'data':Photo})

def Sview(request,sid): 
    Sview=s_product.objects.get(id=sid)
    sp_id=Sview.SpotID
    Spot=spot_db.objects.get(Username=sp_id)
    return render(request,'User/spotview.html',{'proview':Sview,'data':Spot})

def Cview(request,cid): 
    Cview=F_Product.objects.get(id=cid)
    ca_id=Cview.CaterID
    Cater=Cater_DB.objects.get(Username=ca_id)
    return render(request,'User/caterview.html',{'proview':Cview,'data':Cater})

def bookdetails(request):
    uid=request.session['id']
    udata=User_DB.objects.get(id=uid)
    
    ddata=book.objects.filter(userid=uid)
    cdata=C_book.objects.filter(userid=uid)
    sdata=S_book.objects.filter(userid=uid)
    pdata=P_book.objects.filter(userid=uid)

    return render(request,'User/bookdetails.html',{'ddata':ddata, 'sdata':sdata, 'cdata':cdata, 'pdata':pdata,'udata':udata})

def Sbook(request,sid):
    data=s_product.objects.get(id=sid)
    if request.method=="POST":
        
        username=request.POST['username']
        email=request.POST['email']
        number=request.POST['number']
        price=request.POST['price']
        
        pid=sid
        uid=request.session['id']
        cid=data.SpotID

        save_value=S_book(username=username,price=price,email=email,number=number,book=True,prodid=pid,userid=uid,Spotid=cid)
        save_value.save()
        return redirect('uhome')

    return render(request,'User/sbooking.html',{'data':data})
    
    
def Dbook(request,did):
    data=Product.objects.get(id=did)
    if request.method=="POST":
        
        username=request.POST['username']
        email=request.POST['email']
        number=request.POST['number']
        price=request.POST['price']
        
        
        pid=did
        uid=request.session['id']
        cid=data.DecorID

        save_value=book(username=username,price=price,email=email,number=number,book=True,prodid=pid,userid=uid,Decorid=cid)
        save_value.save()
        return redirect('uhome')

    return render(request,'User/dbooking.html',{'data':data})

def Cbook(request,cid):
    data=F_Product.objects.get(id=cid)
    if request.method=="POST":
        
        username=request.POST['username']
        email=request.POST['email']
        number=request.POST['number']
        price=request.POST['price']
        
        pid=cid
        uid=request.session['id']
        cid=data.CaterID

        save_value=C_book(username=username,price=price,email=email,number=number,book=True,prodid=pid,userid=uid,caterid=cid)
        save_value.save()
        return redirect('uhome')

    return render(request,'User/cbooking.html',{'data':data})

def Pbook(request,pid):
    data=P_Product.objects.get(id=pid)
    if request.method=="POST":
        
        username=request.POST['username']
        email=request.POST['email']
        number=request.POST['number']
        price=request.POST['price']
        
        pid=pid
        uid=request.session['id']
        cid=data.CaterID

        save_value=P_book(username=username,price=price,email=email,number=number,book=True,prodid=pid,userid=uid,photoid=cid)
        save_value.save()
        return redirect('uhome')

    return render(request,'User/pbooking.html',{'data':data})
    
def decor_rate(request,id):
    uid=request.session['id']
    if request.method=="POST":

        rate=request.POST['rating']
        review=request.POST['Suggestions']
        book.objects.filter(id=id).update(rate=rate)
        book.objects.filter(id=id).update(review=review)
        
        data=book.objects.get(id=id)
        pid=data.prodid
        data=book.objects.filter(prodid=pid)
        length=len(data)
        # trate=[]
        x=0
        for i in data:
            # trate.append(i.rate)
            x=int(i.rate)+x
        
        trate=int(round(x/length))
        Product.objects.filter(id=pid).update(rate=trate)
        return redirect('bookdetails')
    
    return render(request,'User/rate.html',{'pid':id})

def cater_rate(request,id):
    uid=request.session['id']
    if request.method=="POST":

        rate=request.POST['rating']
        review=request.POST['Suggestions']
        C_book.objects.filter(id=id).update(rate=rate)
        C_book.objects.filter(id=id).update(review=review)
        
        data=C_book.objects.get(id=id)
        pid=data.prodid
        data=C_book.objects.filter(prodid=pid)
        length=len(data)
        # trate=[]
        x=0
        for i in data:
            # trate.append(i.rate)
            x=int(i.rate)+x
        
        trate=int(round(x/length))
        F_Product.objects.filter(id=pid).update(rate=trate)
        
        return redirect('bookdetails')
    
    return render(request,'User/rate.html',{'pid':id})

def spot_rate(request,id):
    uid=request.session['id']
    if request.method=="POST":
        
        rate=request.POST['rating']
        review=request.POST['Suggestions']
        S_book.objects.filter(id=id).update(rate=rate)
        S_book.objects.filter(id=id).update(review=review)
        
        data=S_book.objects.get(id=id)
        pid=data.prodid
        data=S_book.objects.filter(prodid=pid)
        length=len(data)
        # trate=[]
        x=0
        for i in data:
            # trate.append(i.rate)
            x=int(i.rate)+x
        
        trate=int(round(x/length))
        s_product.objects.filter(id=pid).update(rate=trate)
        
        return redirect('bookdetails')
    
    return render(request,'User/rate.html',{'pid':id})

def photo_rate(request,id):
    uid=request.session['id']
    if request.method=="POST":
        
        rate=request.POST['rating'] 
        review=request.POST['Suggestions']
        P_book.objects.filter(id=id).update(rate=rate)
        P_book.objects.filter(id=id).update(review=review)
        
        data=P_book.objects.get(id=id)
        pid=data.prodid
        data=P_book.objects.filter(prodid=pid)
        length=len(data)
        # trate=[]
        x=0
        for i in data:
            # trate.append(i.rate)
            x=int(i.rate)+x
        
        trate=int(round(x/length))
        P_Product.objects.filter(id=pid).update(rate=trate)
        return redirect('bookdetails')
    
    return render(request,'User/rate.html')

def cater_review(request,cid): 
    Cview=C_book.objects.filter(prodid=cid)
    
    return render(request,'User/reviews.html',{'review':Cview})

def decor_review(request,did): 
    Dview=book.objects.filter(prodid=did)
    
    return render(request,'User/reviews.html',{'review':Dview})

def spot_review(request,sid): 
    Sview=S_book.objects.filter(prodid=sid)
    
    return render(request,'User/reviews.html',{'review':Sview})

def photo_review(request,pid): 
    Pview=P_book.objects.filter(prodid=pid)
    
    return render(request,'User/reviews.html',{'review':Pview})

# def pay(request):
#       global amount
#       print(amount)
#       currency ="INR"
#       api_key=RAZORPAY_API_KEY
#       amt=int(amount)*100
#       payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
#       payment_order_id= payment_order['id'] 
#       return render(request,'userfolder/home/pay.html',{'a':amount,'api_key':api_key,
#       'order_id':payment_order_id})

client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
def cpay(request,id):
    global amount
    data=C_book.objects.get(id=id)
    C_book.objects.filter(id=id).update(paystatus=True)
    C_book.objects.filter(id=id).update(accept=False)
    amount=data.price
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'User/pay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

def dpay(request,id):
    global amount
    data=book.objects.get(id=id)
    book.objects.filter(id=id).update(paystatus=True)
    book.objects.filter(id=id).update(accept=False)
    amount=data.price
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'User/pay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

def spay(request,id):
    global amount
    data=S_book.objects.get(id=id)
    S_book.objects.filter(id=id).update(paystatus=True)
    S_book.objects.filter(id=id).update(accept=False)
    amount=data.price
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'User/pay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

def ppay(request,id):
    global amount
    data=P_book.objects.get(id=id)
    P_book.objects.filter(id=id).update(paystatus=True)
    P_book.objects.filter(id=id).update(accept=False)
    amount=data.price
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'User/pay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

# def Cimage(request,sid): 
#     Sview=s_product.objects.get(id=sid)
#     sp_id=Sview.SpotID
#     Spot=spot_db.objects.get(Username=sp_id)
#     return render(request,'User/spotview.html',{'proview':Sview,'data':Spot})

def Cimage(request,cid): 
    Cview=F_image.objects.filter(ProductID=cid)
   
    return render(request,'User/image.html',{'proview':Cview})

def Dimage(request,cid): 
    Cview=D_image.objects.filter(ProductID=cid)
   
    return render(request,'User/image.html',{'proview':Cview})

def Simage(request,cid): 
    Cview=S_image.objects.filter(ProductID=cid)
   
    return render(request,'User/image.html',{'proview':Cview})

def Pimage(request,cid): 
    Cview=P_image.objects.filter(ProductID=cid)
   
    return render(request,'User/image.html',{'proview':Cview})
