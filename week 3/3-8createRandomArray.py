import random
from maxInArray36 import maxInArray

print('생성된 난수중 최댓값을 구합니다')
num = int(input('난수의 갯수 입력 : '))
max = int(input('난수 범위 최댓값 입력 : '))
min = int(input('난수 범위 최솟값 입력 : '))
x= [None] * num

for i in range(len(x)) :
    x[i] = random.randint(min, max)

print(f'{x}')
print(f'이중 최댓값은 {maxInArray(x)}입니다')