from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tables(request):
    return render(request,'tables.html')
   







