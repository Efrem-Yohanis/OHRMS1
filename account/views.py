from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        if hasattr(request.user,'groups'):
                a = request.user.groups.all()[0].name
                if a == 'Admin':
                    return redirect('admin-dashbord',)
                elif a == 'user':
                    return redirect('home')
        else:
            messages.error(request,'You are not authenticated')
            return render(request, 'login.html')

    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            if hasattr(user,'groups'):
                    a = user.groups.all()[0].name
                    if a == 'Admin':
                        login(request, user)
                        return redirect('admin-dashbord',)
                    elif a == 'user':
                        login(request, user)
                        return redirect('home')
            else:
                
                messages.error(request,'Username or password is not correct!')
                return render(request, 'login.html')
    return render(request, 'login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    return redirect('login')


# make crate super order
