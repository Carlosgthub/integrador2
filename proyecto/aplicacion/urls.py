from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu, name="menu"),
    path('registroConExito/', views.registroExito, name="registroConExito"),
    path('RegistroUsuario/', views.RegistroUsuario.as_view(), name="RegistroUsuario"),
    path('informacionUsuario/<int:pk>', views.InformacionUsuario.as_view(), name="InformacionUsuario"),
    path('EditarUsuario/<int:pk>', views.EditarUsuario.as_view(), name="EditarUsuario"),
    path('BajaUsuario/<int:pk>', views.EliminarUsuario, name="EliminarUsuario"),

    path('prueba/', views.dashboard, name='dashbaord'),

    #Urls de juegos
    path('menu/JuegosMatematicas/', views.JuegosMatematicas, name='JuegosMatematicas'),
    path('menu/JuegosEspanol/', views.JuegosEspanol, name='JuegosEspanol'),
    path('menu/JuegosCiencias/', views.JuegosCiencias, name='JuegosCiencias'),
    path('menu/JuegosHistoria/', views.JuegosHistoria, name='JuegosHistoria'),
    path('menu/JuegosCivismo/', views.JuegosCivismo, name='JuegosCivismo'),
    path('menu/JuegosGeografia/', views.JuegosGeografia, name='JuegosGeografia'),
]
