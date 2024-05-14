from django.urls import path, include
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('accounts/', include('allauth.urls')), #? 추가됨
]