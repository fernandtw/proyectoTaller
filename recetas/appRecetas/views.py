from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Post 
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.forms import AuthenticationForm


def is_admin(user):
    return user.is_staff

# Vista de índice
def index(request):
    return render(request, 'base.html')

# Vista de inicio (home)
def home(request):
    recetas = Post.objects.all() #Transforma datos a una lista
    data = {
        'recetas': recetas
    }
    return render(request, 'home.html', data)

# Vista de categoría
def category(request):
    return render(request, 'home.html')

# Vista de recetas
@login_required
def recetas(request):
    recetas = Post.objects.all() #Transforma datos a una lista
    data = {
        'recetas': recetas
    }
    return render(request, 'lista_recetas.html', data)

# Vista de cierre de sesión
def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()  # Guardar el usuario
            login(request, user)  # Iniciar sesión automáticamente
            return redirect('home')  # Redirigir a la página de inicio o donde desees
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@user_passes_test(is_admin)
def agregar_receta(request):
    
    data = {
        'form': PostForm()
    }
    
    if request.method == 'POST':
        formulario = PostForm(data=request.POST, files=request.FILES)  # Crea una instancia del formulario
        if formulario.is_valid():
            formulario.save() 
        else:
            # Si el formulario no es válido, lo volvemos a enviar con los errores
            data = {
                'form': formulario,
                'mensaje': "Hubo un error al guardar la receta."
            }
    else:
        formulario = PostForm()
        data = {
            'form': formulario
        }

    return render(request, 'Admin/agregar.html', data)

@user_passes_test(is_admin)
def listar_recetas(request):
    recetas = Post.objects.all()  # Asegúrate de usar la clase Post correctamente
    data = {
        'recetas': recetas  # Cambia 'Post' por 'recetas' para que sea más descriptivo
    }
    return render(request, 'Admin/listar.html', data)


@user_passes_test(is_admin)
def modificar_receta(request, id):

    receta = get_object_or_404(Post, id=id)

    data  = {
        'form': PostForm(instance=receta)
    }

    if request.method == 'POST':
        formulario = PostForm(data=request.POST, instance=receta, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_recetas")
        data["form"] = formulario

        
    
    return render(request, 'Admin/modificar.html', data)

@user_passes_test(is_admin)
def eliminar_receta(request, id):
    receta = get_object_or_404(Post, id=id)
    receta.delete()
    return redirect(to="listar_recetas")

# Detalle receta

def receta_detalle(request, receta_id):
    receta = get_object_or_404(Post, id=receta_id)
    ingredientes = receta.ingredients.split("\n")  # Convertir los ingredientes en una lista
    instrucciones = receta.instructions.split("\n")  # Convertir las instrucciones en una lista

    context = {
        'receta': receta,
        'ingredientes': ingredientes,
        'instrucciones': instrucciones,
    }
    return render(request, 'recetas/receta_detalle.html', context)
