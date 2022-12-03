from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('This is our first views function')
def propose(request):
    return HttpResponse('<marquee> yes I love u Harsha Bangaram <marquee>')