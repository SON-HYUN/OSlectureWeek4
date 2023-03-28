from typing import Any, Sequence

def maxInArray(a : Sequence) -> Any :
    max = a[0]
    for i in range(1, len(a)) :
        if a[i] > max :
            max = a[i]
    return max

if __name__ == '__main__' :
    print('배열의 최댓값을 구합니다.')
    num = int(input('배열 크기를 입력해주세요 : '))
    x = [None] * num

    for i in range (num) :
        x[i] = int(input(f'x[{i}]값을 입력해주십시오 : '))

    print(f'최댓값은 {maxInArray(x)}입니다')