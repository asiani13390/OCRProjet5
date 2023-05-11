from rest_framework import routers
from django.urls import path, include
from . import views
from p5.views import ProjectsViewset

router = routers.SimpleRouter()
router.register('projects', ProjectsViewset, basename='projects')

urlpatterns = [
    path("", views.index, name="index"),
    path("", include(router.urls)),
]

