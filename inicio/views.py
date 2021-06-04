from django.shortcuts import render
from django.http import HttpResponse

def myHomeView(request, *args, **kwars):
  myContext = {
      'myText': 'Este es sólo un mensaje',
      'myNumber': 123,
      }
  return render(request, "home.html", myContext)

def anotherView(request, *args, **kwars):
  print(args, kwars)
  print(request.user)
  return HttpResponse('<h1>Sólo otra página</h1>')
