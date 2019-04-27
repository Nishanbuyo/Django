from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return HttpResponse("My app is gonna be a <strong> Fantastic </strong> website")