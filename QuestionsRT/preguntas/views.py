from django.views.generic import CreateView
from django.views.generic import ListView, View
from django.http import JsonResponse #Respuestas AJAX

from usuarios.models import Usuario
from .models import Pregunta, Unica_respuesta
from .forms import PreguntaCreateForm

class PreguntaCreateView(CreateView):
    model = Pregunta
    template_name = "preguntas/crearPregunta_form.html"
    form_class = PreguntaCreateForm
    success_msg = "Pregunta creada exitosamente"
    success_url = 'listar-preguntas'


class PreguntasListView(ListView):
    model = Pregunta

    def get_context_data(self, **kwargs):
        context = super(PreguntasListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

class Resultados(ListView):
    model = Pregunta
    template_name = "preguntas/resultados_list.html"

    def get_context_data(self, **kwargs):
        context = super(Resultados, self).get_context_data(**kwargs)

        preguntas = Pregunta.objects.all()
        respuestas_preguntas = Unica_respuesta.objects.all()
        pregunta_FV = []

        for pre in preguntas:

            respuesta = '0'
            if pre.respuesta:
                respuesta = '1'

            buenas = respuestas_preguntas.filter(pregunta=pre.id, respuesta=respuesta)
            malas = respuestas_preguntas.filter(pregunta=pre.id).exclude(respuesta=respuesta)
            pregunta_FV.append({'pregunta': pre, 'buenas': buenas, 'malas':malas})

        context['count'] = self.get_queryset().count()
        context['pregunta_FV'] = pregunta_FV
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