from django import forms
from django.contrib.auth.models import User

TIPO_USUARIO = (
     ('PADRE','PADRE'),
     ('PROFESOR','PROFESOR'),
 )

class CreateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    tipo=forms.ChoiceField(choices=TIPO_USUARIO, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields =('username','password','tipo')