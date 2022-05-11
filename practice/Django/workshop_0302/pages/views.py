from django.shortcuts import render
import datetime
# Create your views here.
def dinner(request, menu, number):
    context = {
        'menu' : menu,
        'number' : number,
    }
    return render(request, 'dinner.html', context)

def test(request):
    menus = ['가', '나', '다']
    today = datetime.datetime.now()
    context = {
        'menus' : menus,
        'today' : today,
    }
    return render(request, 'test.html', context)