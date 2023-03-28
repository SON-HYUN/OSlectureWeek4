# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : 1부터 입력받은 정수 N까지의 연속된 정수들의 합
# 입력이 양수가 아닐때 재입력을 받음

num : int
print('1부터 입력 받은 정수까지 연속된 수의 합을 구합니다.')
while True :
    num =  int(input('숫자를 입력하세요. 숫자는 양수여야만 합니다... : '))
    if num > 0 :
        break

sum = 0
for i in range(1,num+1) :
    sum += i

print('결과값 : %d'%sum)