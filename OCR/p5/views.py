from rest_framework.viewsets import ReadOnlyModelViewSet
from django.http import HttpResponse
from p5.models import Projects
from p5.serializers import ProjectsSerializer

# Create your views here.

def index(request):
    return HttpResponse("Welcome to Openclassrooms project 5.")


class ProjectsViewset(ReadOnlyModelViewSet):

    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return Projects.objects.all()
