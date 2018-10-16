from django.views.generic import CreateView
from django.views.generic import TemplateView, ListView, View
from django.urls import reverse_lazy
from django.http import JsonResponse #Respuestas AJAX

from usuarios.models import Usuario
from .models import Pregunta, Unica_respuesta
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

class RespuestaAjax(View):
    def get(self, request, *args, **kwargs):

        pregunta = Pregunta.objects.get(id = request.GET['idPregunta'])
        estudiante = Usuario.objects.get(id = request.GET['idEstudiante'])

        data = {
            'is_taken': Unica_respuesta.objects.filter(estudiante=estudiante, pregunta=pregunta).exists()
        }

        if data['is_taken']:
            data['error_message'] = 'Ya respondio la pregunta'

        else:
            Unica_respuesta.objects.create(
                estudiante=estudiante,
                pregunta=pregunta,
                respuesta=request.GET['respuesta'],
            )
            data['error_message'] = 'Se envio la respuesta exitosamente!!'


        return JsonResponse(data)