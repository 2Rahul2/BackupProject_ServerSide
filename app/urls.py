from django.urls import path
from .views import *
urlpatterns = [
    path('' , home),
    path('java/', javaRequest),
    path('getToken/' , getToken),
    path('getData/' ,getData),
    path('sendData/' ,getZipFiles),
    path('signin/' ,createAccountPage),
    path('createAccount/' ,createAccount),
    path('tjson/' ,sendJson),
    path('checkCredential/' ,javaSignIn),
    path('data/' ,getUserFiles),


    path('LoginIn' ,loginAccount),
    path("lol/" ,saveFiles),
]
