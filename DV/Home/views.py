from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('Hello World!')



def home(request):
    return render (request,'index.html')
