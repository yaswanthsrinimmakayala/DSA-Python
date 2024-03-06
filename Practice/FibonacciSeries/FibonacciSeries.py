def fibonacci(nthterm):
    a=0
    b=1
    for i in range(2,nthterm+1):
        c = a+b
        a = b
        b = c
    return c

print(fibonacci(4))

