from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.models import *
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import random
import string
from user.serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.

def generate_password(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(length))
    return password

def generate_username(length):
    username_characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(username_characters) for _ in range(length))
    return username

@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        new_user = unapproved.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone)
        if new_user:
            response_data = {
                'code':1000,
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'phone':phone,
                'message': 'Thank you for registering! Your registration has been successful. We will email you the login credentials shortly. Thank you!'
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def manage_user(request):
    search_users = unapproved.objects.filter(activation=True)
    serializer = unapprovedS(search_users, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def all_unapproved(request):
    search_users = unapproved.objects.filter(activation=False)
    serializer = unapprovedS(search_users, many=True)
    return JsonResponse(serializer.data, safe=False)




@api_view(['GET'])
def activate_user(request, user_id):
    try:
        search_user = unapproved.objects.get(id=user_id)
        subject = 'Welcome to OHRMS'
        from_email = settings.EMAIL_HOST_USER  # Replace with the desired sender email address
        to_email = [search_user.email]  # Replace with the recipient email addresses
        password = generate_password(8)
        username = generate_username(6)
        context = {
            'password': password,
            'username': username,
            'search_user': search_user
        }
        new_user = User.objects.create(
            first_name=search_user.first_name,
            last_name=search_user.last_name,
            email=search_user.email,
            username=username,
            password=password
        )
        if new_user:
            search_user.activation = True
            search_user.save()

            html_content = render_to_string('email_template.html', context)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
            email.attach_alternative(html_content, 'text/html')
            email.send()
            
            response_data = {
                'message': 'You have successfully approved.'
            }
            return JsonResponse(response_data, status=200)
    except unapproved.DoesNotExist:
        response_data = {
            'message': 'User does not exist.'
        }
        return JsonResponse(response_data, status=404)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_house(request):
    user = request.user
    user_id = user.id
    req_user = User.objects.get(id=user_id)
    print(req_user)
    if request.method == 'POST':
        location = request.data.get('location')
        price = request.data.get('price')
        description = request.data.get('description')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')

        newhouse = ListingHouse.objects.create(user=req_user, location=location, price=price, description=description, image1=image1, image2=image2, image3=image3, image4=image4)

        if newhouse:
            data = {
                'code': 1000,
                'message': 'Successfully House posted',
                'location': location,
                'price': price
            }
            return Response(data, status=status.HTTP_201_CREATED)


    return Response({"message": "Invalid request"})




class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})