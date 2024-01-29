from django.shortcuts import render, redirect, get_object_or_404

from gymapp.forms import ClienteGimnasioForm

from .models import Profesional, ClienteGimnasio, Servicio

from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.


def index(request):
    context={}
    return render (request, 'gymapp/index.html', context)

def Servicios(request):
    context={}
    return render (request, 'gymapp/Servicios.html', context)

def Nosotros(request):
    context={}
    return render (request, 'gymapp/Nosotros.html', context)

def Entrenadores(request):
    profesionales = Profesional.objects.all()
    context = {'profesionales': profesionales}
    return render(request, 'gymapp/Entrenadores.html', context)



def Contactanos(request):
    context={}
    return render (request, 'gymapp/Contactanos.html', context)

@staff_member_required
def TablaEntrenadores(request):
    profesionales = Profesional.objects.prefetch_related('alumnos').all()
    context = {'profesionales': profesionales}
    return render(request, 'gymapp/TablaEntrenadores.html', context)

def eliminar_alumno(request, alumno_id):
    alumno = get_object_or_404(ClienteGimnasio, pk=alumno_id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('Entrenadores')
    # Maneja el caso si la solicitud no es POST
    return HttpResponse("Solicitud no permitida")

def agregar_cliente_gimnasio(request, profesional_id):
    profesional = get_object_or_404(Profesional, pk=profesional_id)
    if request.method == 'POST':
        form = ClienteGimnasioForm(request.POST)  # Crear el formulario con los datos recibidos
        if form.is_valid():
            # Guarda el formulario pero no lo hace efectivo en la BD aún
            cliente_gimnasio = form.save(commit=False)
            cliente_gimnasio.entrenador = profesional  # Asigna el profesional al cliente
            cliente_gimnasio.save()  # Ahora sí guarda en la BD
            return redirect('Entrenadores')
    else:
        form = ClienteGimnasioForm()  # Crea un formulario vacío si no hay datos POST
    return render(request, 'gymapp/agregar_cliente_gimnasio.html', {'form': form})

