from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages






def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        else:
            if user.is_staff:
                messages.success(request, 'Bienvenido al panel de administración.')
                return redirect('admin_dashboard')
            else:
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



@login_required
def admin_dashboard(request):
    if request.user.is_staff:
        return render(request, 'Panel/admin_dashboard.html')
    else:
        return redirect('home')

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
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('home')  # Redirigir a la página de inicio o donde desees
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# Vista del perfil
# @login_required
# def profile_view(request):
#     return render(request, 'registration/profile.html')  # Asegúrate de tener este template

