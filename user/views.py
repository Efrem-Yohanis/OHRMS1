from django.shortcuts import render
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
   
    # from_email = settings.EMAIL_HOST_USER  # Replace with the desired sender email address
    # to_email = ['efremyohanis116@gmail.com']  # Replace with the recipient email addresses
   
    # # Render the HTML template with the context data
    # html_content = render_to_string('email_template.html', {'variable': 'value'})
    
    # # Create a plain text version of the HTML content
    # text_content = strip_tags(html_content)
    
    # # Create the email message object
    # email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    
    # # Attach the HTML content to the email
    # email.attach_alternative(html_content, 'text/html')
    
    # # Send the email
    # email.send()
    
    # Optionally, you can redirect to a success page or return a success message
    return render(request,'admin_home.html')


def manage_user(request):
    return render(request,'manage_user.html')

def pending_post(request):
    return render(request,'pending_post.html')

def new_account(request):
    return render(request,'new_account.html')


def manage_reques(request):
    return render(request,'manage_reques.html')



def house_detail(request):
    return render(request,'house_detail.html')


def post_house(request):
    return render(request,'post_house.html')


def search_house(request):
    return render(request,'search_house.html')
