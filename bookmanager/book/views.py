from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(req):
    return render(req, 'book/index.html')


def booklist(req):
    return HttpResponse('booklist')


def receive(req):
    data = req.GET
    uname = data.get('uname')
    pwd = data.get('pwd')
    return HttpResponse(f'received,uname:{uname},pwd:{pwd}')
