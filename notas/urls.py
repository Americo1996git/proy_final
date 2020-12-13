
from django.urls import path
from . import views

urlpatterns = [
    path('',views.muro, name='muro'),
    path('nota/nueva/', views.nueva_nota, name='nueva_nota'),##el atributo name lleva el nombre que invocamos en html
    path('nota/<int:pk>/editar/', views.editar_nota, name='editar_nota'),
    #path('publicacion/<int:pk>/eliminar/', views.publicacion_eliminar, name='publicacion_eliminar'),
]