while True:
    n = input("값을 입력하세요:")

    if n=='q':
        print('exit')
        break
    else:
        n = int(n)
        if n % 2 == 0:
            print(n,'은 짝수')
        else:
            print(n,'은 홀수')