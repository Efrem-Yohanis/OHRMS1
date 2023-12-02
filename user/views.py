from django.shortcuts import render

# Create your views here.
def login(request):

    return render(request,'login1.html',{})

def home(request):

    return render(request,'index.html',{})


def registrtion(request):
    
    return render(request,'registration.html',{})