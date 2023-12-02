from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
# Create your views here.
def login(request):

    return render(request,'login1.html',{})

def home(request):

    return render(request,'index.html',{})


def registrtion(request):

    return render(request,'registration.html',{})

def tearm(request):
    
    return render(request,'tearm.html',{})

def admin(request):
    

    # subject = 'Hello from Django'
    # message = 'This is the email content.'
    # from_email = 'ephadaniel177@gmail.com'  # Replace with the desired sender email address
    # recipient_list = ['efremyohanis111@gamil.com']  # Replace with the recipient email addresses

    # send_mail(subject, message, from_email, recipient_list)

    
    return render(request,'admin_home.html',{})