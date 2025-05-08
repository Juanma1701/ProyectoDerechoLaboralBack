from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Users)
class Users(admin.ModelAdmin):
    list_display = ['id','name','last','email','password']
    search_fields = ['Users']

@admin.register(Leyes)
class Leye(admin.ModelAdmin):
    list_display = ['id','name','description']
    search_fields = ['name']