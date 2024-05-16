from django.urls import path#, include
from .views import signup, login, logout#, auth_receiver

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # path('auth-receiver/', auth_receiver, name='auth_receiver'), #? 추가됨
]