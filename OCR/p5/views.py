from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from p5.serializers import ProjectSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from p5.models import Project


def index(request):
    return HttpResponse("Welcome to Openclassrooms project 5.")


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        #authentication = JWTAuthentication()
        #user, token = authentication.authenticate(self.request)

        queryset = Project.objects.all()
        return queryset