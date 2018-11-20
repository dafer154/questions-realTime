from django.conf.urls import url
from .views import ( LogoutTemplateView, UsuarioCreateView, UsuariosListView)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'usuarios'

urlpatterns = [
    url('crear-usuario', UsuarioCreateView.as_view(), name='crear_usuario'),
    url('listar-usuarios', UsuariosListView.as_view(), name='listar_usuarios'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
