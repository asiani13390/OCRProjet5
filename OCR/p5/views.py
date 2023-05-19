from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
import uuid
from .permissions import AllowOnlyPostWithoutAuthentication

from p5.models import Project
from p5.serializers import ProjectSerializer, SignupSerializer



class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        #authentication = JWTAuthentication()
        #user, token = authentication.authenticate(self.request)

        queryset = Project.objects.all()
        return queryset


class SignupAPIView(generics.GenericAPIView):

    serializer_class = SignupSerializer
    permission_classes = [AllowOnlyPostWithoutAuthentication]

    # Eviter l'erreur : 'SignupAPIView' should either include a `queryset` attribute, or override the `get_queryset()` method.
    queryset = User.objects.none()

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        
        if (serializer.is_valid()):
            serializer.save()
            return Response(    {
                                    "RequestId" : str(uuid.uuid4()),
                                    "Message" : "Create user successfuly",
                                    "User" : serializer.data 
                                },
                                status=status.HTTP_201_CREATED )

        return Response(    {
                               "Errors" : serializer.errors 
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )
