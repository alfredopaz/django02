from django.shortcuts import render
from django.http import HttpResponse

def myHomeView(*args, **kwars):
  print(args, kwars)
  return HttpResponse('<h1>Hola Mundo desde Django</h1>')

def anotherView(request, *args, **kwars):
  print(args, kwars)
  print(request.user)
  return HttpResponse('<h1>Sólo otra página</h1>')
