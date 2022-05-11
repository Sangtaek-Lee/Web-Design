from multiprocessing import context
from unicodedata import name
from django.shortcuts import render

# Create your views here.
def search(request):

    return render(request, 'articles/search.html')