from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from p5.serializers import ProjectSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
#from rest_framework import permissions
#from p5.serializers import UserSerializer, GroupSerializer
#from django.http import HttpResponse
#from p5.models import Project

def index(request):
    return HttpResponse("Welcome to Openclassrooms project 5.")


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        authentication = JWTAuthentication()
        user, token = authentication.authenticate(self.request)
        queryset = Projects.objects.all()
        #queryset = Project.objects.filter(author_user_id=user.id)
        return queryset