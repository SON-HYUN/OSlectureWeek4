from maxInArray36 import maxInArray

print('배열의 최댓값을 구합니다')
print('"End" 입력시 입력을 종료합니다')

num = 0
x = []

while True :
    s = input(f'x[{num}]값을 입력해주세요 : ')
    if s == 'End' :
        break
    x.append(int(s))
    num += 1

print(f'{num}개의 숫자를 입력받았습니다')
print(f'최댓값은 {maxInArray(x)}입니다.')