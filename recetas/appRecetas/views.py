from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Post 
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.forms import AuthenticationForm


# Vista de índice
def index(request):
    return render(request, 'base.html')

# Vista de inicio (home)
def home(request):
    return render(request, 'home.html')

# Vista de categoría
def category(request):
    return render(request, 'home.html')

# Vista de publicaciones
def post(request):
    return render(request, 'post.html')

# Vista de recetas
@login_required
def recetas(request):
    return render(request, 'lista_recetas.html')

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

from django.shortcuts import render, redirect
from .forms import PostForm

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

def listar_recetas(request):
    recetas = Post.objects.all()  # Asegúrate de usar la clase Post correctamente
    data = {
        'recetas': recetas  # Cambia 'Post' por 'recetas' para que sea más descriptivo
    }
    return render(request, 'Admin/listar.html', data)
