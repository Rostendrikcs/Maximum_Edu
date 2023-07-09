from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def rep(request):
    return HttpResponse('Домашка по 4 занятию')