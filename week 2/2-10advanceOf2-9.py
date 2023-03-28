# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : 두 숫자 사이의 합 - 계산 과정도 출력

print('입력할 두 숫자 사이의 수를 더해서 출력합니다')
num1 = int(input('첫번째 숫자 : '))
num2 = int(input('두번째 숫자 : '))

if(num1 > num2) :
    num1,num2 = num2,num1

sum = 0
for i in range(num1, num2) :
    sum += i
    print('%d +' %i, end=' ')
sum += num2
print('%d = %d' %(num2, sum))