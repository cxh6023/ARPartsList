from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def arbuilder(request):
    return render(request, 'arbuilder.html')


def buildsearch(request):
    return render(request, 'buildsearch.html')


def partsearch(request):
    return render(request, 'partsearch.html')