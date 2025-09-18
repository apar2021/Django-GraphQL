from django.contrib import admin
from .models import Book
from django.urls import path 
# Register your models here.

admin.site.register(Book)

urlpatterns = [
    path('admin/',admin.site.urls),
]