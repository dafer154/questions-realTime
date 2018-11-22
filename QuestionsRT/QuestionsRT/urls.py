from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('usuarios/', include('usuarios.urls', namespace="gestion_usuarios")),
    path('preguntas/', include('preguntas.urls', namespace="gestion_preguntas")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)