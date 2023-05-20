from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView


from p5.models import Project
from p5.serializers import ProjectSerializer, SignupSerializer



#class SignupAPIView(generics.GenericAPIView):

#class SignupAPIView(APIView):

#    serializer_class = SignupSerializer

    # Permettre à tout le monde de s'enegistrer
#    permission_classes = (AllowAny,)


    # Eviter l'erreur : 'SignupAPIView' should either include a `queryset` attribute, or override the `get_queryset()` method.
#    queryset = User.objects.none()

#    def post(self, request):
#        serializer = self.get_serializer(data = request.data)
#        serializer.is_valid(raise_exception = True)
        
#        if (serializer.is_valid()):
#            serializer.save()
#            return Response( { "User" : serializer.data }, status=status.HTTP_201_CREATED )

#        return Response( { "Errors" : serializer.errors }, status=status.HTTP_400_BAD_REQUEST )




class SignupAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    # https://code.tutsplus.com/tutorials/how-to-authenticate-with-jwt-in-django--cms-30460
    
    
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        user.is_active = True
        serializer = SignupSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response( {"User" : serializer.data }, status=status.HTTP_201_CREATED )

        return Response( { "Errors" : serializer.errors }, status=status.HTTP_400_BAD_REQUEST )











class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset


