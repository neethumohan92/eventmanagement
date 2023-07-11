from django.urls import path
from . import views

urlpatterns = [
    path('shome',views.s_home,name='shome'),
    path('sreg',views.s_register,name='sreg'),
    path('slog',views.S_login,name='slog'),
    
    path('saddpro',views.S_Addpro,name='saddpro'),
    # path('Paddcateg',views.P_Addcateg,name='Paddcateg'),
    path('SViewpage',views.S_Viewpagedecor,name='SViewpage'),
    
    path('simg/<int:cid>',views.addimg,name='simg'),
    
    path('Sdashboard',views.S_dashboard, name='Sdashboard'),
    path('Seditpro/<int:id>',views.S_editpro, name='Seditpro'),
    path('SproDview/<int:tid>',views.S_proDview, name='Sprovw'),
    path('Sproup/<int:id>',views.S_produpdate, name='Sproup'),
    path('Sprodel/<int:pid>',views.S_proddelete, name='Sprodel'),
    path('sbdetails',views.S_bookdetails,name='sbdetails'),
    path('scdetails/<int:cid>',views.S_customerdetails, name='scdetails'),
    path('prodetails/<int:pid>',views.S_productdetails, name='prodetails'),
    
    path('saccept/<int:sid>',views.S_accept, name='saccept'),

    path('sreject/<int:sid>',views.S_reject, name='sreject'),
    










]