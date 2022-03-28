while True:
    
    a=input("첫 번째 숫자를 입력하세요:")

    if a=="00000":
        break
            
    b=int(input("두 번째 숫자를 입력하세요:"))
    a=int(a)

    result = a + b
    print(a, "+",b,"=",result)
            
    result = a - b
    print(a, "-",b,"=",result)

    result = a * b
    print(a, "*",b,"=",result)

    result = a / b
    print(a, "/",b,"=",result)

print("end of program")


