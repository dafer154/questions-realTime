from django.views.generic import CreateView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy

from .models import Pregunta
from .forms import PreguntaCreateForm

class PreguntaCreateView(CreateView):
    model = Pregunta
    template_name = "preguntas/crearPregunta_form.html"
    form_class = PreguntaCreateForm
    success_msg = "Pregunta creada exitosamente"
    success_url = reverse_lazy('gestion_usuarios:listar_usuarios')


class PreguntasListView(ListView):
    model = Pregunta

    def get_context_data(self, **kwargs):
        context = super(PreguntasListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context
