from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from p5.models import Projects

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups','last_name','first_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProjectsSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = ('project_id', 'title', 'description', 'type', 'author_user_id')
        
        
