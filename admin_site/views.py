from django.shortcuts import render,redirect
from user.models import *
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
from django.contrib import messages
# Create your views here.
import random
import string
from django.contrib.auth.models import User

def generate_password(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(length))
    return password

def generate_username(length):
    username_characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(username_characters) for _ in range(length))
    return username

def admin(request):
    user=request.user
    admin=unapproved.objects.get(user=user)
    all_aproved_house=ListingHouse.objects.filter(approval=True).order_by('-crated_date')[:8]
    context = {'all_aproved_house':all_aproved_house,
               'admin':admin}
    for house in all_aproved_house:
        print(house.image1.url)
    return render(request,'admin_home.html',context)


def manage_user(request):
    user=request.user
    admin=unapproved.objects.get(user=user)
    serach_users = unapproved.objects.filter(activation=True)
    context={'serach_user':serach_users,
             'admin':admin}
    print("hello terer")
    return render(request,'manage_user.html',context)

def pending_post(request):
    user=request.user
    admin=unapproved.objects.get(user=user)
    all_huse=ListingHouse.objects.filter(approval=False)
    
    context= {'all_huse':all_huse,
              'admin':admin}
    return render(request,'pending_post.html',context)

def new_account(request):
    user=request.user
    admin=unapproved.objects.get(user=user)
    unapproved_objects = unapproved.objects.filter(activation=False)
    context = {'all_unapproved':unapproved_objects,
               'admin':admin}
    print(unapproved_objects)
    return render(request,'new_account.html',context)

def activate_user(request, user_id):
    user=request.user
    admin=unapproved.objects.get(user=user)
    serach_user = unapproved.objects.get(id=user_id)
    subject = 'Wellcome to OHRMS'
    from_email = settings.EMAIL_HOST_USER  # Replace with the desired sender email address
    to_email = [serach_user.email]  # Replace with the recipient email addresses
    password = generate_password(8)
    username = generate_username(6)
    context ={'password':password,
               'username':username,
               'serach_user':serach_user}
    new_user = User.objects.create(first_name=serach_user.first_name,last_name=serach_user.last_name,email=serach_user.email,username=username,password=password)
    if new_user:
        serach_user.activation = True
        new_user.user = new_user
        serach_user.save()

        html_content = render_to_string('email_template.html',context)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, 'text/html')
        
        email.send()
        messages.success(request,"You have successfully approved.")
        return redirect('manage_user')
    return redirect('new_account')


def reject_user(request, user_id):
    reject_user = unapproved.objects.get(id=user_id)
    reject_user.delete()
    messages.success(request,"You have successfully Reject.")
    return redirect('new_account')



def manage_reques(request):
    user=request.user
    admin=unapproved.objects.get(user=user)
    # all_request = BookingHouse.objects.filter(status='REQUEST_APPROVED', status='REQUEST_ON_PROCESS' )
    all_request = BookingHouse.objects.filter(status__in=['REQUEST_ON_PROCESS'])
    context={'all_request':all_request,
             'admin':admin}
    return render(request,'manage_reques.html',context)


def view_user(request,user_id):
    user=request.user
    admin=unapproved.objects.get(user=user)
    request_user = unapproved.objects.get(id=user_id)
    user=request_user.user
    all_Listing_house=ListingHouse.objects.filter(user=user,approval=True)
    all_bookid_house=BookingHouse.objects.filter(Request_by=user,status='REQUEST_APPROVED')
    total_book=BookingHouse.objects.filter(Request_by=user,status='REQUEST_APPROVED').count()
    total_post=ListingHouse.objects.filter(user=user,approval=True).count()
    context={'request_user':request_user,
             'all_Listing_house':all_Listing_house,
             'all_bookid_house':all_bookid_house,
             'total_book':total_book,
             'total_post':total_post,
             'admin':admin
             }
    return render(request, 'view_user.html',context)


def view_house(request,house_id):
    user=request.user
    admin=unapproved.objects.get(user=user)
    req_house = ListingHouse.objects.get(id=house_id)
    user=req_house.user
    req_account = unapproved.objects.get(user=user)
    
    print(req_account.phone)
    context = {'req_house':req_house,'req_account':req_account,
               'admin':admin}
    return render(request,'house_detail_admin.html',context)
def approve_post_house(request,house_id):
    req_house = ListingHouse.objects.get(id=house_id)
    user=req_house.user
    
    req_house.approval = True
    req_house.save()
    messages.success(request,'You have successfully approved the HOUSE POST request!')
   
    subject='House Listing Approval'
    from_email= settings.EMAIL_HOST_USER
    to_email= [user.email]
    context={'req_house':req_house}
    html_content = render_to_string('email_tempalte2.html',context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, 'text/html')
    email.send()
    return redirect('admin-dashbord')


def reject_post_house(request,house_id):

    req_house = ListingHouse.objects.get(id=house_id)
    user=req_house.user
    req_house.delete()
    messages.success(request,'You have successfully Reject the HOUSE POST request!')
    

    subject='House Listing Reject'
    from_email= settings.EMAIL_HOST_USER
    to_email= [user.email]
    context={'req_house':req_house}
    html_content = render_to_string('email_tempalte3.html',context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, 'text/html')
    email.send()

    return redirect('admin-dashbord')

def approve_booking_request(request,req_id):
    request_house=BookingHouse.objects.get(id=req_id)
    user=request_house.Request_by
    request_house.status = 'REQUEST_APPROVED'
    request_house.save()
    messages.success(request,'You have successfully Approved the house booking request!')
    
    subject='House Booking Request Approval'
    from_email= settings.EMAIL_HOST_USER
    to_email= [user.email]
    context={'req_house':request_house}
    html_content = render_to_string('email_tempalte4.html',context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, 'text/html')
    email.send()

    return redirect('manage-reques')
