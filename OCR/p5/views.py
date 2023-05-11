from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from p5.serializers import UserSerializer, GroupSerializer


from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from p5.models import Projects
from p5.serializers import ProjectsSerializer

# Create your views here.

def index(request):
    return HttpResponse("Welcome to Openclassrooms project 5.")


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return Projects.objects.all()


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