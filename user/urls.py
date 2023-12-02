from django.urls import path,include
from .views import *
urlpatterns = [
   
    path('',login,name='login'),
    path('home',home,name='home'),

]
