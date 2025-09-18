from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
# import sqlite3
# Create your views here.
def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_book.html', context)
def book(request,id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'book.html',context)

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h2>Know More About FirstApp </h2>")

def user(request,name):
    return HttpResponse(f"<h2>Hello {name}. Welcome to home page of the FirstApp.</h2>")