from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
   
    path('',login,name='login'),
    path('home/',home,name='home'),
    path('registration/',registrtion,name='registration'),
    path('tearm-and-condtion/',tearm,name='tearm'),
    
    #  ---------------------------------------------- #
    
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    #---------------------------------------------------------------------------#

    path('admin-dashobord/',admin,name='admin'),
    path('manage_user/',manage_user,name='manage_user'),
    path('pending_post/',pending_post,name='pending_post'),
    path('new_account/',new_account,name='new_account'),
    path('manage_reques/',manage_reques,name='manage-reques'),
    
    # ---------------------------------------------------------------------------- #
    
    path('house_detail/',house_detail,name='house-detail'),
    
]
