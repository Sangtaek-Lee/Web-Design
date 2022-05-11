from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from .models import Article
# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title_get = request.POST.get('title')
    content_get = request.POST.get('content')
    Article.objects.create(title=title_get, content=content_get)

    return redirect('articles:index')