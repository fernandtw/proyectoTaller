from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('recetas/',views.recetas, name="recetas"),
    path('register/',views.register, name="register"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('custom_redirect/', views.custom_redirect, name='custom_redirect'),
    path('logout/',views.exit,name='exit'),
    path('post/', views.post, name='post'),
    path('category/',views.category, name='category'),
    path('adminDashboard/', views.admin_dashboard, name='admin_dashboard'),  # Añadir esta línea
    path('accounts/',include('django.contrib.auth.urls')),


]


