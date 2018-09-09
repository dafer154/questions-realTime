from django.conf.urls import url
from .views import ( PreguntaCreateView, PreguntasListView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^crear-pregunta$', PreguntaCreateView.as_view(), name='crear_pregunta'),
    url(r'^listar-preguntas$', PreguntasListView.as_view(), name='listar_preguntas'),
    #url(r'^classRoom$', ClassRoom.as_view(), name='Classroom'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)