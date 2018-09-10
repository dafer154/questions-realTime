from django.views.generic import CreateView, UpdateView, DetailView, View
from django.views.generic import TemplateView, ListView
#from django.core.urlresolvers import reverse_lazy

from .models import Usuario
from .forms import UsuarioCreateForm

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = "usuarios/usuario_form.html"
    form_class = UsuarioCreateForm
    success_msg = "Usuario creado exitosamente"
    #success_url = reverse_lazy('gestion_usuarios:listar_usuario')


class UsuariosListView(ListView):
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super(UsuariosListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class LogoutTemplateView(TemplateView):
    template_name = "logged_out.html"