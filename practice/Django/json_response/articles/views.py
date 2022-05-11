from urllib import response
from django.shortcuts import HttpResponse, get_object_or_404, render
from articles import serializers
from django.http.response import JsonResponse       # json 형태 response 처리해 준다.
from .models import Article, Comment
from .serializers import (
    ArticleListSerializer,
    ArticleDetailSerializer,
    CommentListSerializer
    )
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

# def article_html(request):
#     articles = Article.objects.all()
#     context = {
#         'articles' : articles
#     }
#     return render(request, 'articles/article.html', context)



# def article_json_1(request):
#     articles = Article.objects.all()
#     article_json = []

#     for article in articles:
#         article_json.append(
#             {
#                 'id' : article.id,
#                 'title' : article.title,
#                 'content' : article.content,
#                 'updated_at' : article.updated_at,
#                 'created_at' : article.created_at,
#             }
#         )

#     return JsonResponse(article_json, safe=False) # safe = True default


# def article_json_2(request):
#     articles = Article.objects.all()
#     data = serializers.serialize('json', articles)
#     return HttpResponse(data, content_type='application/json')

# @api_view(['GET'])
# def article_json_3(request):
#     articles = Article.objects.all()
#     serializer = ArticleListSerializer(articles, many=True)
#     return Response(serializer.data)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"result": "success"}, status=status.HTTP_201_CREATED)
        # return Response({"result": "fail"}, status=status.HTTP_400_BAD_REQUEST)
        



@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete' : f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleDetailSerializer(article, data=request.data, partial=True)  # partial 은 부분 수정가능하게 하는 옵션 (=PACH method)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
def article_comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'GET':
        comments = Comment.objects.filter(article=article)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentListSerializer(comment)
        return Response(serializer.data)


