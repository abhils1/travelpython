from django.http import HttpResponse
from django.shortcuts import render
from .models import Place


# Create your views here.
# def demo(request):
#  return render(request, "indexone.html")
# def operation(request):
#  x=int(request.GET['num1'])
#  y = int(request.GET['num2'])
#  add=x+y
#  sub=y-x
#  div=y/x
#  mul=x*y
#  return render (request,"result.html",{'result':add,'subtract':sub,'divide':div,'multiply':mul})
def demo(request):
    obj = Place.objects.all()
    return render(request, "index.html", {'result': obj})
