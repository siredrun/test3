from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello sire')
def detail(request, p1,p2,p3):
    return HttpResponse('year:%s,mouth:%s,day:%s' % (p1,p2,p3))
