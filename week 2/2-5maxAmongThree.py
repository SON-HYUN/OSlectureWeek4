# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : 세 정수중 최댓값

num1, num2, num3 = [0] * 3
print('정수 세개를 입력하면 최댓값을 구합니다')
num1 = int(input('첫번째 정수 : '))
num2 = int(input('두번째 정수 : '))
num3 = int(input('세번째 정수 : '))

maximum = num1
if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3

print('세 정수중 최댓값 = %d' % maximum)
