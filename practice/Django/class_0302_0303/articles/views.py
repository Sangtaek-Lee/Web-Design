from email import message
from multiprocessing import context
from random import random
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


# def index(request):
#     return HttpResponse('<h1>Hola</h1>')

def index(request):
    return render(request, 'articles/index.html')


# def greeting(request):
#     return render(request, 'greeting.html', {'name':'Alice',})
def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name' : 'Alice',
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    context = {
        'pick':pick,
        'foods':foods,
        }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get("message")
    context = {
        'message' : message,
    }
    # print(message)
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    # print(name, "##########################")
    context = {
        'name' : name,
    }
    return render(request, 'articles/hello.html', context)

def intro(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'articles/intro.html', context)