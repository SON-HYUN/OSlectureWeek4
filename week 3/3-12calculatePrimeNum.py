counter = 0

for i in range (2, 1001) :
    for j in range (2, i) :
        counter += 1
        if i % j == 0 :
            break
    else :
        print(i)
print (f'연산 횟수 : {counter}')