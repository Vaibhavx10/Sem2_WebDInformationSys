from dataclasses import field
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','uname','uemail','upass']
        #To hide password when returning the response
        extra_kwargs = {
            'upass':{'write_only':True}
        }

    def create(self,validated_data):
        # here we are extracting the password
         upass = validated_data.pop('upass',None)
         instance = self.Meta.model(**validated_data)

         if upass is not None:
            #  this will save password in DB under password column name
             instance.set_password(upass)
         instance.save()
         return instance

