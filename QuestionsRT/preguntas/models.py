from django.db import models
from usuarios.models import Usuario

class Pregunta(models.Model):


    respuesta_choices = (
        (0, True),
        (1, False),
    )

    pregunta = models.CharField(verbose_name="Pregunta", max_length=300)
    respuesta = models.BooleanField(verbose_name="Respuesta correcta", choices=respuesta_choices)
    tipo = models.CharField(max_length=70, default="Pregunta de Falso o Verdadero")

    def __str__(self):
        return str(self.pregunta)


class Unica_respuesta(models.Model):
    #cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    respuesta = models.TextField()

    def __str__(self):
        return str(self.pregunta)

