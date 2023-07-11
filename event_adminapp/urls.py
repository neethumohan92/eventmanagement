from django.urls import path
from . import views

urlpatterns = [
    path('home',views.A_home,name='ahome'),
    path('areg',views.A_register,name='areg'),
    path('alog',views.A_login,name='alog'),
    
    # path('Decor_DB/<int:did>',views.D_db,name='Decor_DB'),
    # path('Cater_DB/<int:cid>',views.C_db,name='Cater_DB'),
    # path('Photo_DB/<int:pid>',views.P_db,name='Photo_DB'),
    # path('spot_db/<int:sid>',views.S_db,name='spot_db'),
    
    path('table',views.table,name='table'),
    

]