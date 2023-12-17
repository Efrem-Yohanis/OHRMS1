from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [

    path('',admin,name='admin-dashbord'),
    path('manage_user/',manage_user,name='manage_user'),
    path('pending_post/',pending_post,name='pending_post'),
    path('new_account/',new_account,name='new_account'),
    path('activate_user/<int:user_id>',activate_user,name='activate_user'),
    path('reject_user/<int:user_id>',reject_user,name='reject_user'),
    
    path('view_user/<int:user_id>',view_user,name='view_user'),
    path('manage_reques/',manage_reques,name='manage-reques'),
    path('view_house/<int:house_id>/',view_house,name='view-house'),
    path('approve_post_house/<int:house_id>/',approve_post_house,name='approve_post_house'),
    path('reject_post_house/<int:house_id>/',reject_post_house,name='reject_post_house'),
    
    path('approve_booking_request/<int:req_id>/',approve_booking_request,name='approve_booking_request'),
    

    
]
