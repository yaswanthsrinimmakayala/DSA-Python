def fib(x,f):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if f[x]!=0:
        return f[x]
    else:
        f[x] = fib(x-1,f)+fib(x-2,f)
    return f[x]

x =4
f = [0]*(x+1)
print(fib(x,f))