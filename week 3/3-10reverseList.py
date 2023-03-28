from typing import Any, MutableSequence

def reverseList(arr : MutableSequence) -> None :
    size = len(arr)
    for i in range (size // 2) :
        arr[i], arr[size - 1 - i] = arr[size - 1 - i], arr[i]

if __name__ == '__main__' :
    print('리스트 원소를 역순으로 뒤집습니다')
    size = int(input('원소의 갯수를 입력해주세요 : '))
    arr = [None] * size

    for i in range(size) :
        arr[i] = int(input(f'x[{i}] 값을 입력해주십시오 : '))

    reverseList(arr)
    print('뒤집은 배열은 다음과 같습니다 : ')
    for i in range(size) :
        print(f'x[{i}]= {arr[i]}')