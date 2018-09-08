from django.db import models
from django.contrib.auth.models import User, Group, Permission

class Usuario(User):

    perfil_usuario = (
        (0, 'Profesor'),
        (1, 'Estudiante'),

    )

    perfil_usuario = models.IntegerField(choices=perfil_usuario, verbose_name="Perfil de usuario", default=0)
    imagen_perfil = models.ImageField(verbose_name="Imagen de perfil", upload_to='imagenes_perfil/', null=True)
