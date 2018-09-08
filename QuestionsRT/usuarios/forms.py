from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': ("Contraseña")})) #Nuevo campo
password2 = forms.CharField(label="Contraseña (confirmación)", widget=forms.PasswordInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': ("Confirma tu contraseña")}))
username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': ("Usuario")}))

class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        exclude = ('is_active', 'last_login', 'groups', 'user_permissions', 'is_staff', 'date_joined', 'is_superuser',)
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name',
                  'email','perfil_usuario', 'imagen_perfil')
