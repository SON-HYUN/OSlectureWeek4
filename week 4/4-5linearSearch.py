# 선형 검색

from typing import Any, Sequence

def seqSearch(arr : Sequence, key : Any) :
    i = 0
    while True :
        if i == len(arr) :
            return -1
        if arr[i] == key :
            return i
        i += 1

if __name__ == '__main__' :
    num = int(input('원소 수를 입력하세요. : '))
    arr = [None] * num
    
    for i in range(num) :
        arr[i] = int(input(f'arr[{i}] = '))
    
    key = int(input('검색할 값을 입력하세요 : '))
        
    index = seqSearch(arr, key)
        
    if index == -1 :
        print('찾고자 하는 값이 배열에 없습니다')
    else :
        print(f'찾고자 하는 값은 arr[{index}] 에 있습니다.')
