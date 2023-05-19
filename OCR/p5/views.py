from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from p5.serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated


from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from p5.models import Project
from p5.serializers import ProjectsSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication

def index(request):
    return HttpResponse("Welcome to Openclassrooms project 5.")


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        authentication = JWTAuthentication()
        user, token = authentication.authenticate(self.request)
        #queryset = Projects.objects.all()
        queryset = Project.objects.filter(author_user_id=user.id)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]