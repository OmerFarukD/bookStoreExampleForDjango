from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author

def index(request):
    return HttpResponse('Anasayfa')
def authors(request):
    template=loader.get_template('authors.html')
    context={
        'author_list':Author.objects.all()
    }
    return HttpResponse(template.render(context,request))
def books(request):
    return HttpResponse('kitaplar')
def authorDetails(request,authorId):
   # template=loader.get_template('authorDetail.html')
    context={
        'author_detail':Author.objects.get(pk=authorId)
    }
    return render(request,'authorDetail.html',context)
