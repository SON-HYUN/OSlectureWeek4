counter = 0
index = 0
prime = [None] * 500

prime[index] = 2
index += 1
prime[index] = 3
index += 1
print('2')
print('3')

for i in range (5, 1001, 2) :
    j = 1
    while(prime[j] * prime[j] <= i) :
        counter += 2
        j += 1
        if i % prime[j] == 0 :
            break
    else :
        prime[index] = i
        index += 1
        print(i)
        counter += 1
print (f'연산 횟수 : {counter}')