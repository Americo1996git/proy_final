from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Nota
from django.utils import timezone
from .forms import NotaForm
#from django.contrib.auth.decorators import login_required

# Create your views here.
def muro(request):
    notas = Nota.objects.all()
    return render(request,'notas/muro.html',{'notas': notas})

def nueva_nota(request):
    if request.method == "POST":
        formulario = NotaForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('muro')
    else:
        formulario = NotaForm()
    return render(request, 'notas/editar_nota.html', {'formulario': formulario})

def editar_nota(request, pk):
    publicacion = get_object_or_404(Nota, pk=pk)
    if request.method == "POST":
        formulario = NotaForm(request.POST, instance=publicacion)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.published_date = timezone.now()
            publicacion.save()
            return redirect('muro')
    else:
        formulario = NotaForm(instance=publicacion)
    return render(request, 'notas/editar_nota.html', {'formulario': formulario})