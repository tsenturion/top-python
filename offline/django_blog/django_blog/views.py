from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

def about(requests):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        requests,
        'about.html',
        context={'tags': tags},
        )

def med_info_view(request, user_id, pet_id):
    return render(
        request,
        'med_info.html',
        context={'user_id': user_id, 'pet_id': pet_id, 'source': 'global'},
    )