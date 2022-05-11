from re import A
from django.shortcuts import render, redirect

import articles
from .models import Article

# Create your views here.
def index(request):
    # DB의 데이터를 모두 가져오는 방법
    # 모델을 이용해 모든 데이터 가져온다.
    # articles = Article.objects.all()[::-1]    # 데이터를 가져 와서 정렬한다.
    articles = Article.objects.order_by('-pk')  # 데이터를 가져올 때 부터 정렬한다. 내림차순은 - 붙여준다.

    # 가져온 데이터를 템플릿으로 넘긴다
    context = {
        'articles' : articles,
    }
    # 템플릿에서 데이터를 보여준다.
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title_get = request.POST.get('title')
    content_get = request.POST.get('content')
    article = Article(title=title_get, content=content_get)
    article.save()

    return redirect('articles:detail', article.pk)   # 바로 인덱스로 page로 가고 싶다면 render 로 불러오는게 아닌 redirect로 직접 간다.
                                        # render로 불러 온다면 article 불러오는 문구를 한번 더 써줘야 된다.

def detail(request, pk):
    article = Article.objects.get(pk=pk)  # 데이터를 가져올 때 부터 정렬한다. 내림차순은 - 붙여준다.
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)



def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':                # URL 로 조작하지 못하도록 POST방식일때만 delete 하도록 조건문건다.
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return  render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)