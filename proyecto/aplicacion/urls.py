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
]
