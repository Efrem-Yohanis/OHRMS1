from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import Field
from .models import *
from django.contrib import messages
# Create your views here.


def home(request):
    user=request.user
    request_account=unapproved.objects.get(user=user)
    all_aproved_house=ListingHouse.objects.filter(approval=True).order_by('-crated_date')[:8]
    context = {'all_aproved_house':all_aproved_house,'request_account':request_account}
    
    return render(request,'index.html',context)


def registrtion(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_pic=request.FILES.get('profile_pic')


        new_user=unapproved.objects.create(first_name=first_name,last_name=last_name,email=email,phone=phone,profile_pic=profile_pic)
        if new_user:
            messages.success(request,'Thank you for registering! Your registration has been successful. We will email you the login credentials shortly. Thank you!')
            return redirect('login')
        # Process the form data as needed

    return render(request,'registration.html',{})

def tearm(request):
    
    return render(request,'tearm.html',{})




def house_detail(request,house_id):
    user=request.user
    request_account=unapproved.objects.get(user=user)
    req_house = ListingHouse.objects.get(id=house_id)
    user=req_house.user
    req_account = unapproved.objects.get(user=user)
    
    context = {'req_house':req_house,'req_account':req_account,'request_account':request_account}
    return render(request,'house_detail.html',context)


def post_house(request):
    user=request.user
    request_account=unapproved.objects.get(user=user)
    user=request.user
    user_Id=user.id
    req_user= User.objects.get(id=user_Id)
    print(req_user)
    if request.method == 'POST':

        location = request.POST.get('location')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')

        newhouse=ListingHouse.objects.create(user=req_user,location=location,price=price,description=description,image1=image1,image2=image2,image3=image3,image4=image4)
        if newhouse:
            messages.success(request,'You have successfully posted your house. The administrator will review and approve your post. Thank you for submitting your listing!')
            return redirect('home')
    return render(request,'post_house.html',{'request_account':request_account})


def search_house(request):
    user=request.user
    request_account=unapproved.objects.get(user=user)
    context = {'request_account':request_account}
    return render(request,'search_house.html',context)

def house_booking(request,house_id):
    user=request.user
    request_account=unapproved.objects.get(user=user)
    context = {'request_account':request_account}

    return render(request,'',context)
