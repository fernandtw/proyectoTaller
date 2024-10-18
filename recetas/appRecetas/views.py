from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista de administración
@login_required
def admin(request):
    if request.user.is_staff:
        return redirect('admin')  # Redirigir al panel de administración
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

# Vista de registro
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            if user:
                login(request, user)
                return redirect('profile')  # Redirigir al perfil después del registro

    return render(request, 'registration/register.html', data)

# Vista del perfil
# @login_required
# def profile_view(request):
#     return render(request, 'registration/profile.html')  # Asegúrate de tener este template

