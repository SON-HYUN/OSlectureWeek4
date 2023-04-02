inputStr, outputStr = "", ""
count, i = 0, 0

inputStr = input("문자열을 입력하세요 : ")
count = len(inputStr)

for i in range(count) :
    outputStr += inputStr[count - (i + 1)]

print(f"문자열을 뒤집어 출력합니다 >> {outputStr}")
