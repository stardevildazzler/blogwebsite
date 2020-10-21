from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from .models import quary, userdetail
from django.contrib import messages
import math


def home(request):
    if request.method == 'POST':
        usernamex = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('Email')
        pass1 = request.POST.get('Pass1')
        pass2 = request.POST.get('Pass2')

        x = int(len(pass1))
        y = usernamex.isalnum()
        z = (firstname.isalpha() and lastname.isalpha()
             and usernamex.isnumeric() == False)

        def username_present(usernamex):
            if User.objects.filter(username=usernamex).exists():
                return True

            return False
        if username_present(usernamex) == False:

            if pass1 == pass2 and x > 8 and z:
                if usernamex.isalpha() or y:
                    details = User.objects.create_user(usernamex, email, pass1)
                    details.first_name = firstname
                    details.last_name = lastname
                    details.save()

                    messages.success(request, 'User register sucessfully')
            else:
                messages.error(request, 'Password are not mathed')
        else:
            messages.error(request, 'User alredy exits')
    return render(request, 'content/home.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        quary1 = request.POST.get('quary1')
        details = quary(name=name, email=email, number=number,
                        subject=subject, quary1=quary1)
        details.save()
        messages.success(request, 'Profile details updated.')

    return render(request, 'content/contact.html')


def about(request):
    return render(request, 'content/about.html')


def handle_login(request):
    if request.method == 'POST':
        loginusername = request.POST.get('username')
        loginpassword = request.POST.get('password')
        user = auth.authenticate(
            request, username=loginusername, password=loginpassword)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you  have loggdin successfully')
            return render(request, 'content/home.html')
        else:
            messages.error(request, 'inviled details ')
            return render(request, 'content/home.html')
    return HttpResponse('404 page not found')


def handle_logout(request):

    auth.logout(request)
    messages.success(request, 'loggdout sucessfully ')
    return render(request, 'content/home.html')
    # return HttpResponse('404 page not found')
