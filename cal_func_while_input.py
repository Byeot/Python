def add(a, b):
    return a+b

def minus(a,b):
    return a-b

def multi(a,b):
    return a*b

def divide(a,b):
    return a/b


while True:
    a= input("1st input")
    if a == "00000" :
        break
    a = int(a)
    b= int(input("2nd input"))
    ad=add(a,b)
    mi=minus(a,b)
    mu=multi(a,b)
    di=divide(a,b)
    print("add =", ad)
    print("minus =", mi)
    print("multi =", mu)
    print("divide =", di)
print("Exit Calculator")