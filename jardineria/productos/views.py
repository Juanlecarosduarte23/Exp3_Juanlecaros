from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm,RegistroUserForm,ContactoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def somos(request):
    return render(request, 'somos.html')
def galeria(request):
    return render(request, 'galeria.html')
def contacto(request):
    return render(request, 'contacto.html')            

@login_required
def otra(request):
    plantas = Producto.objects.raw('Select * from productos_producto')
    datos={
        'productos':plantas
    }
    return render(request, 'otra.html', datos)

@login_required
def otra2(request):
    plantas = Producto.objects.raw('Select * from productos_producto')
    datos={
        'productos':plantas
    }
    return render(request, 'otra2.html', datos)



    '''
    autitos = Vehiculo.objects.all()    #similar al select * from Vehiculo
    datos ={
        'vehiculos':autitos
    }
    return render(request, 'otra.html', datos)
    '''
@login_required
def crear(request):
    if request.method=="POST":
        productoform=ProductoForm(request.POST,request.FILES)
        if productoform.is_valid():
            productoform.save()     #similar al insert en función
            return redirect ('otra')
    else:
        productoform=ProductoForm()
    return render (request, 'crear.html', {'productoform': productoform})



def contacto(request):
    if request.method=="POST":
        contactoform=ContactoForm(request.POST,request.FILES)
        if contactoform.is_valid():
            contactoform.save()     #similar al insert en función
            return redirect ('otra2')
    else:
        contactoform=ContactoForm()
    return render (request, 'contacto.html', {'contactoform': contactoform})



@login_required
def eliminar(request, id): 
    productoEliminado = Producto.objects.get(nombre=id) #similar a select * from... where...
    productoEliminado.delete()
    return redirect ('otra')

@login_required
def eliminar2(request, id): 
    ContactoEliminado = Producto.objects.get(usuario=id) #similar a select * from... where...
    ContactoEliminado.delete()
    return redirect ('otra2')

@login_required
def modificar(request, id): 
    productoModificado=Producto.objects.get(nombre=id) #buscamos el objeto
    datos ={
        'form':ProductoForm(instance=productoModificado)
    }
    if request.method=="POST":
        formulario = ProductoForm(data=request.POST, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect ('otra')
    return render(request, 'modificar.html', datos)


@login_required
def modificar2(request, id): 
    contactoModificado=contacto.objects.get(nombre=id) #buscamos el objeto
    datos ={
        'form':ContactoForm(instance=productoModificado)
    }
    if request.method=="POST":
        formulario = ContactoForm(data=request.POST, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect ('otra')
    return render(request, 'modificar2.html', datos)

def registrar(request):
    data = {
        'form' : RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                                password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect ('index')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def mostrar(request):
    plantas = Producto.objects.all()
    datos={
        'plantas': plantas
    }
    return render(request, 'mostrar.html', datos)

def mostrar2(request):
    plantas = Producto.objects.all()
    datos={
        'plantas': plantas
    }
    return render(request, 'mostrar2.html', datos)


