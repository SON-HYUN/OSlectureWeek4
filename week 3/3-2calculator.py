select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

select = int(input("1. 입력한 계산식 계산    2. 두 수 사이의 합 "))
if select == 1 :
    numStr = input("수식 입력 : ")
    answer = eval(numStr)
    print("%s 결과는 %d입니다." %(numStr, answer))
elif select == 2 :
    num1 = int(input("*** 첫번째 숫자 입력 : "))
    num2 = int(input("*** 두번째 숫자 입력 : "))
    for i in range(num1,num2+1) :
        answer += i
    print("두 수 %d와 %d 사이의 합은 %d입니다." %(num1, num2, answer))
else :
    print("잘못된 입력입니다.")