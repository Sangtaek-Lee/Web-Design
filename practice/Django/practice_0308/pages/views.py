from django.shortcuts import render
import requests
from random import randint, random
# Create your views here.
def lotto(request):
    response = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1')
    data = response.json()
    numbers = []
    for i in range(1,7):
        numbers.append(data.get(f'drwtNo{i}'))
    print(numbers)
    bnusNo = data.get('bnusNo')
    cnt_list = [0]*6
        
    numbers_list = []
    for i in range(1000):
        temp_list = []
        cnt = 0
        while len(temp_list) < 7:
            temp = randint(1,45)
            if temp not in temp_list:
                temp_list.append(temp)
                if temp in numbers:
                    cnt += 1
        temp_list.sort()
        numbers_list.append(temp_list)
            
        if cnt == 6:
            cnt_list[0] += 1
        elif cnt == 5:
            if bnusNo in temp_list:
                cnt_list[1] += 1
            else:
                cnt_list[2] += 1
        elif cnt == 4:
            cnt_list[3] += 1
        elif cnt ==3:
            cnt_list[4] += 1
        else:
            cnt_list[5] += 1


    context = {
        'numbers' : numbers,
        'bnusNo' : bnusNo,
        'cnt_list' : cnt_list
    }
    return render(request, 'pages/lotto.html', context)



