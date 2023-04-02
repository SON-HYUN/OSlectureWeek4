# 이분 탐색

from typing import Any, Sequence

def binSearch(arr : Sequence, key : Any) -> int :
    l = 0; r = len(arr) - 1

    while l <= r :
        m = (l + r) // 2
        if arr[m] == key :
            return m
        if arr[m] < key :
            l = m + 1
            continue
        r = m - 1

    return -1

if __name__ == '__main__' :
    num = int(input('원소 갯수를 입력하세요 '))
    arr = [None] * num

    print('배열 데이터를 오름차순으로 입력해주세요 ')

    arr[0] = int(input('arr[0] = '))

    for i in range(1, num) :
        while True :
            arr[i] = int(input(f'arr[{i}] = '))
            if arr[i] >= arr[i - 1] :
                break

    key = int(input('검색할 값을 입력하세요 : '))

    index = binSearch(arr, key)

    if index == -1 :
        print('목표 값이 배열내에 없습니다')
    else :
        print(f'목표 값은 arr[{index}]에 있습니다')
