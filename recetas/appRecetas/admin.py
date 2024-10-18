from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created', 'updated')
    readonly_fields = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)



#POST
class PostAdmin(admin.ModelAdmin): 
    readonly_fields = ['created', 'update']
    list_display = ('title', 'category', 'published', 'author', 'created')
    ordering = ('author','created')
    search_fields = ('title',)


    



admin.site.register(Post, PostAdmin)
