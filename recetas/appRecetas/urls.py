from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('recetas/',views.recetas, name="recetas"),
    path('register/',views.register, name="register"),
    path('login/', views.login, name='login'),
    path('logout/',views.exit,name='exit'),
    path('post/', views.post, name='post'),
    path('category/',views.category, name='category'),
    path('agregar-recetas/',views.agregar_receta, name='agregar_recetas'),
    path('listar-recetas/',views.listar_recetas, name='listar_recetas'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('modificar-receta/<id>/',views.modificar_receta, name='modificar_receta'),
    path('eliminar-receta/<id>/', views.eliminar_receta, name='eliminar_receta'),



]


