"""QuestionsRT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path(r'^login/$', login, name='login'),
    path('logout', logout, name='logout'),
    path('usuarios/', include('usuarios.urls', namespace="gestion_usuarios")),
    path('preguntas/', include('preguntas.urls', namespace="gestion_preguntas")),

    #url('login', login, name='login'),
    #url('logout', logout, {'next_page': 'inicio'}, name='logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)