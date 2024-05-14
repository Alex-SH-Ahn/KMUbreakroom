from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import UserProfile
from posts.models import LOCATIONS

def signup(request):
    error_message = None
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email = request.POST['email']
                )
                print('user okay')
                profile = UserProfile.objects.create(
                    user=user,
                    nickname=request.POST['nickname'],
                    student_number=request.POST.get('student_number', None),
                    major=request.POST.get('major', None),
                )
                print('profile okay')
                profile.save()
                print('profile saved')
                auth.login(request, user)
                print('login and move to home')
                return redirect('home')
            except Exception as e:
                error_message = str(e).split('\n')[0]  # Extract the first line of the error message
                print(f'error: {error_message}')
        else:
            print('password does not match')
            error_message = 'password does not match'
    else:
        print('not a POST request')
    return render(request, 'signup.html', {'error': error_message, 'locations': LOCATIONS})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember = request.POST.get('remember', None)
        
        user = authenticate(request, username=username, password=password)
        print('user authenticated')
        if user is not None:
            auth.login(request, user)
            if remember:
                request.session.set_expiry(1209600) # 2주가 지나면 자동 로그아웃
            else:
                request.session.set_expiry(0)
            return redirect('home')
        else:
            return render(request, 'login.html', {'locations': LOCATIONS})
    return render(request, 'login.html', {'locations': LOCATIONS})

def logout(request):
    auth.logout(request)
    print('user logged out')
    return redirect('/')