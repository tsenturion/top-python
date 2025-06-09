"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_blog import views
from django_blog.views import IndexView, about, med_info_view

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path("about/", views.about),
    path('articles/', include("django_blog.article.urls")),
    #path(route, view)
    #/users/~bob/books/
    path('project/', include("django_blog.project.urls")),
    path('users/<int:user_id>/pets/<int:pet_id>/med_info/', med_info_view),
    path(
        '<int:user_id>/pets/<int:pet_id>/med_info/',
        views.med_info_view,
        name='pet_med_info',
    ),
]
