from django.shortcuts import render
from django.http import HttpResponse

def myHomeView(*args, **kwars):
  return HttpResponse('<h1>Hola Mundo desde Django</h1>')

def anotherView(request, *args, **kwars):
  return HttpResponse('<h1>Sólo otra página</h1>')
