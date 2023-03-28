print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1 = int(input('1번학생의 점수 입력 : '))
score2 = int(input('2번학생의 점수 입력 : '))
score3 = int(input('3번학생의 점수 입력 : '))
score4 = int(input('4번학생의 점수 입력 : '))
score5 = int(input('5번학생의 점수 입력 : '))

total = score1 + score2 + score3 + score4 + score5
print(f'점수 합계는{total}점 입니다.')
print(f'점수 평균은{total/5}점 입니다.')