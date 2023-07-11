from django.urls import path
from . import views

urlpatterns = [
    path('chome',views.C_home,name='chome'),
    path('creg',views.C_register,name='creg'),

    path('clog',views.C_login,name='clog'),
    path('caddpro',views.C_Addpro,name='caddpro'),
    path('addimg/<int:cid>',views.addimg,name='addimg'),
    
    # path('Caddcateg',views.C_Addcateg,name='Caddcateg'),
    path('CViewpage',views.C_Viewpagedecor,name='CViewpage'),
    path('Cdashboard',views.C_dashboard, name='Cdashboard'),
    path('Ceditpro/<int:id>',views.C_editpro, name='Ceditpro'),
    path('CproDview/<int:tid>',views.C_proDview, name='Cprovw'),
    path('Cproup/<int:id>',views.C_produpdate, name='Cproup'),
    path('Cprodel/<int:pid>',views.C_proddelete, name='Cprodel'),
    path('cbdetails',views.C_bookdetails,name='cbdetails'),
    path('ccdetails/<int:cid>',views.C_customerdetails, name='ccdetails'),
    path('cpdetails/<int:pid>',views.C_productdetails, name='cpdetails'),
    
    path('caccept/<int:sid>',views.C_accept, name='caccept'),

    path('creject/<int:sid>',views.C_reject, name='creject'),









]