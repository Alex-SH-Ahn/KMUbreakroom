# from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate#, login as auth_login
from .models import UserProfile
from posts.models import LOCATIONS
# import os
# from django.views.decorators.csrf import csrf_exempt
# from google.oauth2 import id_token
# from google.auth.transport import requests
# import jwt
# from django.utils.decorators import method_decorator
# from rest_framework.views import APIView
# from . import models

def signup(request):
    error_message = None
    print('Initial error message:', error_message)
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
                print('Error message after form submission:', error_message)
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

#*--------------------------------- Google OAuth ---------------------------------

# # def sign_in(request):
# #     return render(request, 'sign_in.html')

# @csrf_exempt
# def auth_receiver(request):
#     print('google auth receiver')
#     """
#     Google calls this URL after the user has signed in with their Google account.
#     """
#     #? token = request.POST['credential']
#     token = request.POST.get('credential')
#     if not token:
#         return HttpResponse(status=400)
#     try:
#         user_data = id_token.verify_oauth2_token(
#             token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
#         )
#     except ValueError:
#         return HttpResponse(status=403)

#     # In a real app, I'd also save any new user here to the database. See below for a real example I wrote for Photon Designer.
#     # You could also authenticate the user here using the details from Google (https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-in)
#     request.session['user_data'] = user_data
#     #? user = authenticate(request, user_data=user_data)
#     #? if user is not None:
#     #?     login(request, user)
#     #? Authenticate the user with Django
#     email = user_data.get("email")
#     user, created = User.objects.get_or_create(
#         email=email, defaults={
#             'username': email,
#             'first_name': user_data.get('given_name', ''),
#             'last_name': user_data.get('family_name', '')
#         }
#     )
#     if created:
#         UserProfile.objects.create(user=user)  # Create user profile if needed
#     auth_login(request, user)

#     return redirect('home')

# #* Save the user to the database
# @method_decorator(csrf_exempt, name='dispatch')
# class AuthGoogle(APIView):
#     def post(self, request, *args, **kwargs):
#         #! Google calls this URL after the user has signed in with their Google account
#         try:
#             user_data = self.get_google_user_data(request)
#         except ValueError:
#             return HttpResponse("Invalid Google token", status=403)

#         email = user_data["email"]
#         user, created = models.User.objects.get_or_create(
#             email=email, defaults={
#                 "username": email, "sign_up_method": "google",
#                 "first_name": user_data.get("given_name"),
#             }
#         )
#         auth_login(request, user)
#         return HttpResponse(status=200)
    
#     @staticmethod
#     def get_google_user_data(request: HttpRequest):
#         token = request.POST['credential']
#         if not token:
#             raise ValueError("No token provided")
#         return id_token.verify_oauth2_token(token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID'])
