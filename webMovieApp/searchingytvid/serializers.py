from dataclasses import field, fields
from rest_framework import serializers
from .models import UsersSubscription




class userssubscriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsersSubscription
        fields =  ['id','typevideocontent','imdbid','videoid','userid']