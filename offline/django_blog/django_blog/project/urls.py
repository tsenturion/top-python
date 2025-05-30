from django.urls import path, include
from django_blog.project.users import views

urlpatterns = [
    path("users/", include("django_blog.project.users.urls")),
]
