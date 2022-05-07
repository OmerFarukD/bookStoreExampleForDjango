from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Anasayfa')
def authors(request):
    return HttpResponse('Yazarlar')
def books(request):
    return HttpResponse('kitaplar')
def authorDetails(request,authorId):
    return HttpResponse('Yazar detayı :'+str(authorId))
