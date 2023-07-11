from django.urls import path
from . import views

urlpatterns = [
    path('dhome',views.D_home,name='dhome'),
    path('dreg',views.D_register,name='dreg'),

    path('dlog',views.D_login,name='dlog'),
    path('addpro',views.Addpro,name='addpro'),
    path('addcateg',views.Addcateg,name='addcateg'),
    path('Viewpage',views.Viewpagedecor,name='Viewpage'),
    
    path('dimg/<int:did>',views.addimg,name='dimg'),
    
    path('dashboard',views.dashboard, name='dashboard'),
    path('editpro/<int:id>',views.editpro, name='editpro'),
    path('proDview/<int:tid>',views.proDview, name='provw'),
    path('proup/<int:id>',views.produpdate, name='proup'),
    path('prodel/<int:pid>',views.proddelete, name='prodel'),
    path('bdeatails',views.bookdetails,name='bdetails'),
    path('cdetails/<int:did>',views.customerdetails, name='cdetails'),
    path('pdetails/<int:pid>',views.productdetails, name='pdetails'),
    
    path('daccept/<int:sid>',views.D_accept, name='daccept'),

    path('dreject/<int:sid>',views.D_reject, name='dreject'),











]