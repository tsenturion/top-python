from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

def index(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")

class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))