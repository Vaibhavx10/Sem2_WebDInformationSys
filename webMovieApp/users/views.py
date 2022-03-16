from lib2to3.pgen2 import token
from multiprocessing.sharedctypes import Value
from random import random
from urllib import request
import jwt,datetime
from django.http import JsonResponse


from logging import raiseExceptions
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from users import serializers
from django.contrib import messages



def returnLoginPage(request):
    return render(request,'users/login.html')


def returnRegisterationPage(request):
    return render(request,'users/registerationPage.html')


class InsertRegisterationInfoToDB(APIView):    
    def post(self,request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_valid(raise_exception=True)
            print(serializer.errors)
            serializer.save() 
            return Response(request.data, status=status.HTTP_200_OK)
        else:
            print("PRINTED ERROR ", serializer.errors)
            return Response(request.data, status=status.HTTP_404_NOT_FOUND)






class RegisterationPage(APIView):
    def post(self,request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class loginAPIAuthentication(APIView):
    def post(self,request):
        uemail = request.data['uemail']
        password = request.data['upass']
        user = User.objects.filter(uemail=uemail).first()

        if user is None:  
            passtoView = {
                "messages":'User not found !!',
                "display":'display:inline-block'
                }
            return render(request, 'users/login.html',passtoView)
            # raise AuthenticationFailed('User not found !!')

        if not user.check_password(password):
            passtoView = {
                "messages":'Incorrect password !!',
                "display":'display:inline-block'
                }
            return render(request, 'users/login.html',passtoView)
            # raise AuthenticationFailed('Incorrect password !!')


        #Using JWT for auth    
        #It will create a JWT while login and save to cookies so from next time 
        #when the user logins his jwt token will be used to validate
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }


        jwttoken = jwt.encode(payload,'secret',algorithm='HS256')

        
        passtoView = {
            'jwtcookie':jwttoken,
            'uemail':uemail,
            'userid':user.id
         }
        print("loginAPIAuthentication | passtoView >> ",user.id)
        response = render(request, 'searchingytvid/subscribeddashboard.html',passtoView)  # django.http.HttpResponse
        response.set_cookie(key='jwtcookie',value=jwttoken,httponly=True)
        return response
        


#Validate the jwt and tell if its proper or not
#Before Every Page call this will be called to check if the user is authenticated and proper
#Soemthing like preconstruct if we get the token from this and then only the user is authenticated using jwt
#jwt will be passed in header everytime for authentication
class getUserDetails(APIView):
    def get(self,request):
    # def get(request):
        token = request.COOKIES.get('jwtcookie')

        if not token:
            raise AuthenticationFailed('Unauthenticated User !!!')

        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token Expired !!')   

        print('payload :: ',payload['id'])
        print('payload :: ',payload)
        userInfo = User.objects.filter(id=payload['id']).first()
        print('user2 :: ',userInfo)
        #user = User.objects.filter(id=payload['id'])
        
        serializer = UserSerializer(userInfo)
        return Response(serializer.data)
        
        
class logoutPage(APIView):
    def post(self,request):
        #Remove the cookie
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'success'
        }
        return response
