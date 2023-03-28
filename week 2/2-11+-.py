# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : +- 번갈아 출력하기

numberOfChar = int(input('입력한 숫자만큼 +과 -를 번갈아가며 출력합니다 \n 문자 갯수를 입력하세요 : '))

for _ in range(numberOfChar // 2):
    print('+-', end='')

if numberOfChar % 2 == 1:
    print('+')