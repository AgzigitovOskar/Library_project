from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Библиотека")


def book(request):
    return HttpResponse("Книги")


def reader(request):
    return HttpResponse("Читатели")


def author(request):
    return HttpResponse("Авторы")
