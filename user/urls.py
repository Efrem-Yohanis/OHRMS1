from django.urls import path,include
from .views import *
urlpatterns = [
   
    path('',login,name='login'),
    path('home/',home,name='home'),
    path('registration/',registrtion,name='registration'),
    path('tearm-and-condtion/',tearm,name='tearm'),
    path('admin-dashobord/',admin,name='admin'),
]
