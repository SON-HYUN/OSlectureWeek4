# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : 이등변삼각형 출력, 중첩 for문

length = int(input('직각이등변삼각형을 출력합니다. \n 짧은 변의 길이를 입력하십시오 : '))

for i in range(1,length+1) :
    for _ in range(i) :
        print('*',end='')
    print()