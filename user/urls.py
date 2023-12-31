from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
   
 
    path(' ',home,name='home'),
    path('registration/',registrtion,name='registration'),
    path('tearm-and-condtion/',tearm,name='tearm'),
    
    #  ---------------------------------------------- #
    
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
    
    # ---------------------------------------------------------------------------- #
    
    path('house_detail/<int:house_id>/',house_detail,name='house-detail'),
    path('post_house/',post_house,name='post-house'),
    path('search_house/',search_house,name='search-house'),
    path('house_booking/<int:house_id>/',house_booking,name='house_booking'),
    
    
    
    
]
