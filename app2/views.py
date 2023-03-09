from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def ayesha(request):
    return HttpResponse('<h1>ayesha is good girl</h1>')
