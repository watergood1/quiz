from django.shortcuts import render
from . import views
from django.http import HttpResponse

def home(request):
    return HttpResponse("books:")

def info(request):
    return HttpResponse("info")

def for_books_html(request):
    book_items =  [
    {"name": "harry potter", "page": 100},
    {"name": "The Hobbit", "page": 247},
    {"name": "Atomic Habits", "page": 362},
    {"name": "1984", "page": 354}

    ]

    context = {
        "book_items": book_items
    }

    return render(request, "books.html", context)


# Create your views here.