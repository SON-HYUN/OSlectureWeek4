# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : 진수 변환기

numeralSelection = int(input('입력할 숫자의 진법(2/8/10/16)'))
num = input('숫자 입력 : ')

num10 = int(num,numeralSelection)

print('16진수 = %s' %(hex(num10)))
print('10진수 = %s' %num10)
print('8진수 = %s' %oct(num10))
print('2진수 = %s' %bin(num10))