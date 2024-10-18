# Generated by Django 5.1.1 on 2024-10-10 22:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Titulo')),
                ('excerpt', models.TextField(verbose_name='Bajada')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts', verbose_name='Imagen')),
                ('published', models.BooleanField(default=False, verbose_name='Publicado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRecetas.category', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
                'ordering': ['-created'],
            },
        ),
    ]
