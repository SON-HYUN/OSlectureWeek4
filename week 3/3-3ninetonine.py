i,k,guguLine = 0, 0, ""

for i in range(2, 10) :
    guguLine = guguLine + (f' # {i}단　#')

print(guguLine)

for i in range(1, 10) :
    guguLine = ''
    for k in range(2, 10) :
        guguLine = guguLine + ('  %dx%d=%2d' %(i,k,i*k))
    print(guguLine)