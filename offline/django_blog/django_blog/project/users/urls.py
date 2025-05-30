from django.urls import path
from django_blog.project.users import views

urlpatterns = [
    path("", views.users_view),
    path("<int:user_id>/pets/<int:pet_id>/med_info/", views.pet_med_info_view),
]
