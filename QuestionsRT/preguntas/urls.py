from django.conf.urls import url
from .views import ( PreguntaCreateView, PreguntasListView, RespuestaAjax, Resultados)
from django.conf import settings
from django.conf.urls.static import static


app_name = 'preguntas'

urlpatterns = [
    url('crear-pregunta', PreguntaCreateView.as_view(), name='crear_pregunta'),
    url('listar-preguntas', PreguntasListView.as_view(), name='listar_preguntas'),
    url('resultados', Resultados.as_view(), name='resultados'),
    url('respuesta', RespuestaAjax.as_view(), name='respuesta')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)