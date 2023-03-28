def radixConvert(x : int, r = int) -> str :
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(str(x))

    print(f'{r:2} | {x:{length}d}')
    while x > 0 :
        print('   +' + (length+2) * '-')
        if x // r :
            print(f'{r:2} | {x // r:{length}d} ... {x % r}')
        else :
            print(f'     {x // r:{length}d} ... {x % r}')
        d += dchar[x % r]
        x //= r

    return d[::-1]

if __name__ == '__main__' :
    print('10진수를 n진수로 변환합니다')
    print()
    while True :
        num = int(input('변환할 10진수의 음이 아닌 정수를 입력해주십시오 : '))
        numSystem = int(input('몇 진수로 변환하시겠습니까? : '))
        result = radixConvert(num, numSystem)
        ch = ''
        print(f'{numSystem}진수의 값은 {result}입니다')
        ch = input('한 번 더 변환하겠습니까? (Y/N) : ')
        if ch in {'N', 'n'} :
            break