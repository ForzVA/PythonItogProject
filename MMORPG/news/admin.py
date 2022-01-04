from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date_creation', 'author', 'category')


admin.site.register(Post, PostAdmin)

# Register your models here.
