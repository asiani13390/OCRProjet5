from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from p5.models import Project
from django.contrib.auth.models import User 


class SignupSerializer(serializers.ModelSerializer):
# https://code.tutsplus.com/tutorials/how-to-authenticate-with-jwt-in-django--cms-30460

    date_joined = serializers.ReadOnlyField()

    class Meta:

        model = User
        fields = ( 'first_name', 'last_name', 'username','email', 'password','date_joined')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        return User.objects.create_user(**data)


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ('__all__')  
