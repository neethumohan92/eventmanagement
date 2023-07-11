from django.urls import path
from . import views

urlpatterns = [
    path('uhome',views.uhome,name='uhome'),
    path('ureg',views.uregister,name='ureg'),
    path('ulog',views.ulogin,name='ulog'),
    
    path('decor',views.Decorations,name='decor'),
    path('spot',views.Locations,name='spot'),
    path('photo',views.Photography,name='photo'),
    path('cater',views.Caterings,name='cater'),
    
    path('decor/<int:did>',views.Dview,name='decor'),
    path('spot/<int:sid>',views.Sview,name='spot'),
    path('photo/<int:pid>',views.Pview,name='photo'),
    path('cater/<int:cid>',views.Cview,name='cater'),
    
    path('cimage/<int:cid>',views.Cimage,name='cimage'),
    path('simage/<int:cid>',views.Simage,name='simage'),
    path('dimage/<int:cid>',views.Dimage,name='dimage'),
    path('pimage/<int:cid>',views.Pimage,name='pimage'),
    
    
    
    path('dbook/<int:did>',views.Dbook,name='dbook'),
    path('cbook/<int:cid>',views.Cbook,name='cbook'),
    path('pbook/<int:pid>',views.Pbook,name='pbook'),
    path('sbook/<int:sid>',views.Sbook,name='sbook'),
    
    path('dashboard',views.Dashboard,name='dashboard'),
    path('editpro/<int:uid>',views.Editpro,name='editpro'),
    path('bookdetails',views.bookdetails,name='bookdetails'),
    
    path('decor_rate/<int:id>',views.decor_rate,name='decor_rate'),
    path('cater_rate/<int:id>',views.cater_rate,name='cater_rate'),
    path('spot_rate/<int:id>',views.spot_rate,name='spot_rate'),
    path('photo_rate/<int:id>',views.photo_rate,name='photo_rate'),
    
    path('decor_review/<int:did>',views.decor_review,name='decor_review'),
    path('cater_review/<int:cid>',views.cater_review,name='cater_review'),
    path('spot_review/<int:sid>',views.spot_review,name='spot_review'),
    path('photo_review/<int:pid>',views.photo_review,name='photo_review'),
    
    path('cpay/<int:id>',views.cpay,name='cpay'),
    path('dpay/<int:id>',views.dpay,name='dpay'),
    path('spay/<int:id>',views.spay,name='spay'),
    path('ppay/<int:id>',views.ppay,name='ppay'),
    
    
    
    

]