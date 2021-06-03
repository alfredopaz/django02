from django.shortcuts import render
from django.http import HttpResponse

def myHomeView(*args, **kwars):
  return HttpResponse('<h1>Hola Mundo desde Django</h1>')
