from django.urls import path
from django_blog.article import views
from django_blog.article.views import ArticleIndexView, index

urlpatterns = [
    path("", ArticleIndexView.as_view(), name="article-index"),
    path("<str:tags>/<int:article_id>/", views.index, name="article"),
]