# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : 동전 교환기

money = int(input('금액 입력 : '))
coin500,coin100,coin50,coin10 = [0] *4
originMoney = money

coin500 = money//500
money %= 500
coin100 = money//100
money %= 100
coin50 = money//50
money %= 50
coin10 = money//10
money %= 10

if originMoney != money+coin500*500+coin100*100+coin50*50+coin10*10 :
    print('error in change')

print('500원 동전 = %d개' %coin500)
print('100원 동전 = %d개' %coin100)
print('50원 동전 = %d개' %coin50)
print('10원 동전 = %d개' %coin10)
print('동전으로 못바꾼 금액 = %d원' %money)