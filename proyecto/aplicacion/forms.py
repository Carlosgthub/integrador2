from django import forms
from django.contrib.auth.models import User

TIPO_USUARIO = (
     ('Niño','Niño'),
     ('Padre','Padre'),
     ('Profesor','Profesor'),
 )

class CrearUsuarioForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=20, label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre(s)', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellidos', widget=forms.TextInput(attrs={'class':'form-control'}))
    school = forms.CharField(max_length=30, label='Escuela', widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.ChoiceField(choices = TIPO_USUARIO, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields =('username','password','tipo','first_name','last_name', 'school')

class EditarUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, label='Nombre(s)', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellidos', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields =('first_name','last_name')