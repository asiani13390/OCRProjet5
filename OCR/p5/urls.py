from rest_framework import routers
from django.urls import path, include
from . import views
from p5.views import ProjectsViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register('projects', ProjectsViewset, basename='projects')

urlpatterns = [
    #path("", views.index, name="index"),
    path("", include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    


]