from django.shortcuts import redirect, render
import time
import math


# Create your views here.
def index(request):
    num = 0
    lst=[]
    count = 0

    if 'cal' in request.POST:
        input_num = request.POST['input_num']
        #input_num 값이 없을 때
        if input_num == '':
            return redirect('index')
        else:
            num = int(input_num)
            print(num)
            
    
            #소수 개수 구하기
            for i in range(2, int(math.sqrt(num)+1)):
                if is_prime(i):
                    lst.append(i)
            for l in range(2, num+1):
                if is_prime(l):
                    count += 1
            print(count)

            return render(request, 'sample/index.html', {'input_num': num, 'result':count})


    # GET
    else:
        return render(request, 'sample/index.html')

# 소수 판별
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True