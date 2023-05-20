from rest_framework import routers
from django.urls import path, include
from . import views
from p5.views import ProjectsViewset
from p5.views import SignupAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register('projects', ProjectsViewset, basename='projects')

urlpatterns = [

    # Utilisateurs
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='TokenRefreshView'),


    # Projets
    path("", include(router.urls)),
    

]