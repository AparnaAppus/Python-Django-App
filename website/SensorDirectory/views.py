from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    template = 'index.html'
    return render(request, template)


def asset(request):
    template = 'test.html'
    return render(request, template)

