from django.db import models

#Basic user details are provide by django we need to 
#override them to make it as per our own customization
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    uname = models.CharField(max_length=255)
    uemail = models.CharField(max_length=255,unique=True)
    upass = models.CharField(max_length=255)
    username = None

    typeofcontentprefered = models.TextField(null=True)
    address = models.TextField(null=True)
    moviessubscribed = models.TextField(null=True)
    age = models.TextField(null=True)
    genre = models.TextField(null=True)
    gender = models.TextField(null=True)
    role = models.TextField(default='guest')


    # Django by default uses usnname and password so we are overiding it to use 
    # uemail as username
    USERNAME_FIELD = 'uemail'
    REQUIRED_FIELDS = []
    


