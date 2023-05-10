from django.urls import path
from . import views
#from .views import project_details
from p5.views import ProjectView


urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", ProjectView.as_view()),
]

