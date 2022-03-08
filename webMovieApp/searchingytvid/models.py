from django.db import models

from users.models import User

# Create your models here.


class UsersSubscription(models.Model):
    typevideocontent = models.CharField(max_length=255)
    imdbid = models.CharField(max_length=255)
    videoid = models.CharField(max_length=255)
    userid = models.ForeignKey(User,on_delete=models.DO_NOTHING)



