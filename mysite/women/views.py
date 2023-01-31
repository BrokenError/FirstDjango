from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения women.")


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям.</h1><p>{catid}</p>")
# Create your views here.

def archive(request, year):
    if int(year) < 2020:
        return redirect('home', permanent=True)  # постоянное перенаправление на другой постоянный url (permanent=true)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')