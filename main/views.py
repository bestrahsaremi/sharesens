from django.views.generic import ListView
from .models import Sentences

class HomeView(ListView):
    model = Sentences
    template_name = 'home.html'
    context_object_name = 'sentences'