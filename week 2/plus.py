# 소프트웨어학부 2학년 손의현 (2020039083)
# 오픈소스기초프로젝트 1주차 과제 : 간단 계산기

a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

result = a + b
print(a, "+", b, "=", result)
result = a - b
print(a, "-", b, "=", result)
result = a * b
print(a, "*", b, "=", result)
result = float(a / b)
print(a, "/", b, "=", result)