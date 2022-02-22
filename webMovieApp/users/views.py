from lib2to3.pgen2 import token
from multiprocessing.sharedctypes import Value
from random import random
import jwt,datetime

from logging import raiseExceptions
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
from users import serializers



class RegisterationPage(APIView):
    def post(self,request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class loginPage(APIView):
    def post(self,request):
        uemail = request.data['uemail']
        password = request.data['upass']

        user = User.objects.filter(uemail=uemail).first()

        if user is None:
            raise AuthenticationFailed('User not found !!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password !!')


        #Using JWT for auth    
        #It will create a JWT while login and save to cookies so from next time 
        #when the user logins his jwt token will be used to validate
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }


        jwttoken = jwt.encode(payload,'secret',algorithm='HS256')

        authresponse = Response()

        authresponse.set_cookie(key='jwtcookie',value=jwttoken,httponly=True)

        authresponse.data = {
            'jwtcookie':jwttoken
        }

        return authresponse

#Validate the jwt and tell if its proper or not
#Before Every Page call this will be called to check if the user is authenticated and proper
#Soemthing like preconstruct if we get the token from this and then only the user is authenticated using jwt
class getUserDetails(APIView):
    def get(self,request):
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



