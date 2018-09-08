from django.conf.urls import url
from .views import ( LogoutTemplateView, UsuarioCreateView, UsuariosListView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^crear-usuario$', UsuarioCreateView.as_view(), name='crear_usuario'),
    url(r'^listar-usuarios$', UsuariosListView.as_view(), name='listar_usuarios'),

    url(r'^log-out$', LogoutTemplateView.as_view(), name='logout_2'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
