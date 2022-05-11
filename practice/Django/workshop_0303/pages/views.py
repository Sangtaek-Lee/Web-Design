from multiprocessing import context
from django.shortcuts import render
import random
# Create your views here.

def lotto(request):
    lotto = []
    while len(lotto)<6:
        num = random.randint(1,46)
        if num not in lotto:
            lotto.append(num)
    context = {
        'lotto' : lotto
    }
    return render(request, 'lotto.html', context)