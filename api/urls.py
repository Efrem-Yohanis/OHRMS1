from django.urls import path
from .views import CustomAuthToken
from . import views

urlpatterns = [
    path('registration/', views.registration),
    path('get_all_approved/', views.manage_user),
    path('get_all_unapproved/', views.all_unapproved),
    path('api/activate_user/<int:user_id>/', views.activate_user,), 
    path('api-token-auth/', CustomAuthToken.as_view()),

    path('post_house/', views.post_house), 
    
    # Add more URL patterns here
]
