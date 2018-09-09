from django import forms
from .models import Pregunta


class PreguntaCreateForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ('pregunta', 'respuesta', 'tipo')