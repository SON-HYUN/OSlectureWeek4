# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : 정수의 부호 구하기

num = int(input('정수 입력 :'))

if num > 0:
    print('숫자 %d는 양수' %num)
elif num == 0:
    print('입력한 숫자는 0')
else:
    print('숫자 %d는 음수' %num)