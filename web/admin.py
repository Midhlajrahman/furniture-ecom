from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date') 
    prepopulated_fields = {'slug': ('title',)} 
    search_fields = ('title', 'description')
    list_filter = ('date',) 
    ordering = ('-date',)
    