counter = 0
index = 0
prime = [None] * 500

prime[index] = 2
index += 1
print('2')

for i in range (3, 1001, 2) :
    for j in range (1, index) :
        counter += 1
        if i % prime[j] == 0 :
            break
    else :
        prime[index] = i
        index += 1
        print(i)
print (f'연산 횟수 : {counter}')