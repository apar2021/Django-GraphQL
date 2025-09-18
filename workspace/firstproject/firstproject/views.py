from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from firstapp.models import Book

def book(request,id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'book.html',context)

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("<h2>Know More About FirstApp </h2>")