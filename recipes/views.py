from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Home page 1')


def about(request):
    return HttpResponse('About Page 1')


def contact(request):
    return HttpResponse('Contact page 1')
