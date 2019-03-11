from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import CreateUserForm

# Create your views here.
def index(request):
    return render(request, 'inicio.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def registroExito(request):
    return render(request, 'registroConExito.html', {})

class RegistroUsuario(CreateView):
    success_url = reverse_lazy('registroConExito')
    template_name = 'RegistroUsuario.html'
    model = User
    form_class = CreateUserForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
