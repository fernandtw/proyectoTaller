from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('recetas/',views.recetas, name="recetas"),
    path('register/',views.register, name="register"),
    path('logout/',views.exit,name='exit'),
    path('post/', views.post, name='post'),
    path('category/',views.category, name='category'),
    path('admin/', views.admin, name='admin'),
]


