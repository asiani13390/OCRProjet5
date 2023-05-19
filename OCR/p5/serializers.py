from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from p5.models import Project
from django.contrib.auth.models import User 



class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ('__all__')  


class SignupSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = (  'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)

        if User.objects.filter(email=email).exists():
            raise serializers.validationError({'email': ('email already exists')})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username' : ('username already exists')})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
