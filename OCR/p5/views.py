from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from p5.models import Projects
from p5.serializers import ProjectSerializer

# Create your views here.

def index(request):
    return HttpResponse("Welcome to Openclassrooms project 5.")


class ProjectView(APIView):

    def get(self, *args, **kwargs):
        queryset = Projects.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
