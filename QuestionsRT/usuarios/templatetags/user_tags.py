from django import template
register = template.Library()
from usuarios.models import Usuario


@register.filter(name = 'has_group')
def has_group(user, group_type):

    print("hello")

    user_group=Usuario.objects.get(pk=user.id)

    if(user_group.perfil_usuario == group_type):
        return True
    else:
        False

@register.filter(name = 'contador')
def any_function(user):


    user_group = Usuario.objects.get(pk=user.id)

    print(user_group)

    if user_group:
        return True
    else:
        return False
