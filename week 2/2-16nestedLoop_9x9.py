# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 2주차 과제 : 구구단 표 출력, 중첩 for문

print('-'*27)
for i in range(1,10) :
    for j in range(1,10) :
        print(f'{i*j : 3} ',end='')
    print()
print('-'*27)