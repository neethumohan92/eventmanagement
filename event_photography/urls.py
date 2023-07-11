from django.urls import path
from . import views

urlpatterns = [
    path('phome',views.P_home,name='phome'),
    path('preg',views.P_register,name='preg'),

    path('plog',views.P_login,name='plog'),
    path('paddpro',views.P_Addpro,name='paddpro'),
    path('Paddcateg',views.P_Addcateg,name='Paddcateg'),
    path('PViewpage',views.P_Viewpagedecor,name='PViewpage'),
    
    path('pimg/<int:cid>',views.addimg,name='pimg'),
    
    path('Pdashboard',views.P_dashboard, name='Pdashboard'),
    path('Peditpro/<int:id>',views.P_editpro, name='Peditpro'),
    path('PproDview/<int:tid>',views.P_proDview, name='Pprovw'),
    path('Pproup/<int:id>',views.P_produpdate, name='Pproup'),
    path('Pprodel/<int:pid>',views.P_proddelete, name='Pprodel'),
    path('pbdetails',views.P_bookdetails,name='pbdetails'),
    path('pcdetails/<int:cid>',views.P_customerdetails, name='pcdetails'),
    path('prdetails/<int:pid>',views.P_productdetails, name='prdetails'),
    
     path('paccept/<int:sid>',views.P_accept, name='paccept'),

    path('preject/<int:sid>',views.P_reject, name='preject'),









]