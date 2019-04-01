from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import CrearUsuarioForm, EditarUsuarioForm

# Create your views here.


def index(request):
    return render(request, 'inicio.html', {})


def registroExito(request):
    return render(request, 'registroConExito.html', {})


# Views de juegos

def JuegosMatematicas(request):
    return render(request, 'math.html', {})


def JuegosEspanol(request):
    return render(request, 'espanol.html', {})


def JuegosCiencias(request):
    return render(request, 'ciencias.html', {})


def JuegosHistoria(request):
    return render(request, 'historia.html', {})


def JuegosCivismo(request):
    return render(request, 'civismo.html', {})


def JuegosGeografia(request):
    return render(request, 'geografia.html', {})


def dashboard(request):
    # if request.user.crearusuario.tipo == 'Profesor':
    #     return redirect('dashboard')

    # if request.user.crearusuario.tipo == 'Niño':
    #     return redirect('menu')
    return render(request, 'dashboard.html', {})


def menu(request):
    
    return render(request, 'menu.html', {})


class RegistroUsuario(CreateView):
    success_url = reverse_lazy('registroConExito')
    template_name = 'RegistroUsuario.html'
    model = User
    form_class = CrearUsuarioForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return redirect(self.get_success_url())


class InformacionUsuario(generic.DetailView):
    model = User
    template_name = "informacionUsuario.html"


class EditarUsuario(UpdateView):
    success_url = reverse_lazy('menu')
    template_name = 'EditarUsuario.html'
    model = User
    form_class = EditarUsuarioForm

# class EliminarUsuario(DeleteView):
#     success_url = reverse_lazy('index')
#     template_name = 'EliminarUsuario.html'
#     model = User


def EliminarUsuario(request, pk):
    try:
        user = User.objects.get(id=pk)
        user.is_active = False
        user.save()
    except Exception as e:
        raise Http404
    return redirect('index')
